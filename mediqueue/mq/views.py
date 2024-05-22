from datetime import datetime, timedelta
from django.utils import timezone
from background_task import background
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordResetView
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseNotAllowed, JsonResponse, \
    HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView
from django import forms
from django.contrib.auth.tokens import default_token_generator as token_generator
from mediqueue import settings
from mq.forms import RegisterUserForm, LoginUserForm, PasswordResetForm, CustomPasswordResetForm
from mq.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .signals import email_remind
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage


# Контроллер для отображения главной страницы
def index(request):
    return render(request, 'mq/index.html')

# Контроллер для отображения профиля пользователя
def account(request):
    user_profile = request.user.userprofile
    today = datetime.today().date()
    afterBooking = today + timedelta(minutes=30)
    bookings = Booking.objects.filter(patient=request.user)
    context = {
        'bookings' : bookings,
        'today' : today,
        'afterBooking' : afterBooking,
    }
    return render(request, 'mq/profile.html', context)


# Контроллер для отображения страницы регистрации пользователя
def registration(request):
    return render(request, 'mq/registration.html')


# Контроллер для обработки страницы "Страница не найдена"
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

# Класс для обработки подтверждения email
class EmailVerify(View):
    def get(self, request, uidb64, token):
        User = get_user_model()
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.save()
            user_profile = UserProfile.objects.get(user=user)
            user_profile.email_verified = True
            user_profile.save()

            return render(request, 'mq/email_confirmation.html')
        else:
            return HttpResponse('Activation link is invalid!')


# Класс для переопределения сброса пароля
class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = '/password_reset/done/'


# Класс для регистрации нового пользователя
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'mq/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_user_context(self, **kwargs):
        return kwargs

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()

        UserProfile.objects.create(
            user=user,
            phone_number=form.cleaned_data.get('phone_number'),
            birth_date=form.cleaned_data.get('birth_date')
        )

        current_site = get_current_site(self.request)
        mail_subject = 'Подтверждение почты на сайте.'
        message = render_to_string('mq/verify_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return redirect('confirm_email')

# Класс для аутентификации пользователя
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'mq/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None and user.userprofile.email_verified:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return redirect('invalid_verify')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
    def get_user_context(self, **kwargs):
        return kwargs

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        phone_number = cleaned_data.get('phone_number')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user_profile = UserProfile.objects.get(user__username=username)
                if user_profile.phone_number != phone_number:
                    raise forms.ValidationError("Неправильный номер телефона.")
            except UserProfile.DoesNotExist:
                raise forms.ValidationError("Неправильное имя пользователя.")

        return cleaned_data

    def get_success_url(self):
        return reverse_lazy('home')

# Класс для отправки подтверждения email
class SendVerificationEmail(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.email_verified:
            #send_email_for_verify(user)
            return JsonResponse({'message': 'Email verification sent.'})
        else:
            return JsonResponse({'message': 'Email is already verified.'})

# Функция для выхода пользователя
def logout_user(request):
    logout(request)
    return redirect('home')

# Функция для отображения списка специализаций
def spec_list(request):
    spec = Category.objects.all().distinct()
    total_count = spec.count()
    half_count = total_count // 2
    first_half = spec[:half_count]
    second_half = spec[half_count:]
    return render(request, 'mq/doctors.html', {'first_half': first_half, 'second_half': second_half})

# Функция для отображения информации о пациенте
def info_pat(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile
    }
    return render(request, 'index.html', context)

# Функция для бронирования
def booking(request, cat_id):
    doctors = Doctors.objects.filter(cat_id=cat_id)
    bookings = Booking.objects.all()

    working_hours = ['08:00', '08:30', '09:00', '09:30', '10:00',
                     '10:30', '11:00', '11:30', '12:00', '12:30',
                     '13:00', '13:30', '14:00', '14:30', '15:00',
                     '15:30', '16:00', '16:30', '17:00', '17:30',
                     '18:00', '18:30', '19:00', '19:30']
    yesterday = datetime.today()
    min_day_value = yesterday.strftime("%Y-%m-%d")
    max_day_value = (yesterday + timedelta(days=14)).strftime("%Y-%m-%d")

    appoints = Booking.objects.filter(booking_date=request.GET.get('date'),
                                      doctor_id=request.GET.get('doctor_id')).all()
    for obj in appoints:
        time_str = obj.time_start.strftime("%H:%M")
        if time_str in working_hours:
            working_hours.remove(time_str)


    if request.GET.get('date')   is None:
        context = {
            'min_day_value': min_day_value,
            'max_day_value': max_day_value,
            'working_hours': working_hours,
            'cat_id': cat_id,
            'doctors': doctors,
            'appoints': appoints,
            'step_1' : True,
            'step' : 'Шаг 1',
        }
        return render(request, 'mq/booking.html', context)
    else:
        context = {
            'min_day_value': min_day_value,
            'max_day_value': max_day_value,
            'working_hours': working_hours,
            'cat_id': cat_id,
            'doctors': doctors,
            'appoints': appoints,
            'step_1' : False,
            'step_2' : True,
            'step' : 'Шаг 2',
        }
        return render(request, 'mq/booking.html', context)

# Функция для подтверждения записи
@csrf_protect
def confirm_booking(request):
    if request.method == 'POST':
        patient = request.user
        doctor_id = request.POST.get('doctor_id')
        date = request.POST.get('date')
        time_start = request.POST.get('time_start')
        doctor = get_object_or_404(Doctors, id=doctor_id)

        existing_booking = Booking.objects.filter(
            patient=patient,
            doctor=doctor,
            booking_date=date,
        ).exists()
        if existing_booking:
            existing_time = Booking.objects.get(
                patient=patient,
                doctor=doctor,
                booking_date=date,
            ).time_start
            return render(request, 'mq/booking_exist.html',
                          {'doctor': doctor, 'date': date, 'existing_time': existing_time})

        if existing_booking:
            return render(request, 'mq/booking_exist.html', {'doctor': doctor, 'date': date, 'time_start': time_start})

        new_booking = Booking(
            patient=patient,
            doctor=doctor,
            booking_date=date,
            time_start=time_start,
            is_cancelled=False,
        )
        try:
            new_booking.full_clean()
        except ValidationError as e:
            error_message = e.message_dict
            return HttpResponse("Ошибка: {}".format(error_message))
        new_booking.save()

        appoints = Booking.objects.filter(booking_date=date, doctor=doctor).values_list('time_start', flat=True)

        doctors = Doctors.objects.filter(cat_id=doctor.cat_id)
        working_hours = ['08:00', '08:30', '09:00', '09:30', '10:00',
                         '10:30', '11:00', '11:30', '12:00', '12:30',
                         '13:00', '13:30', '14:00', '14:30', '15:00',
                         '15:30', '16:00', '16:30', '17:00', '17:30',
                         '18:00', '18:30', '19:00', '19:30']
        for appointment_time in appoints:
            if appointment_time.strftime("%H:%M") in working_hours:
                working_hours.remove(appointment_time.strftime("%H:%M"))
        if time_start in working_hours:
            working_hours.remove(time_start)

        yesterday = datetime.today()
        min_day_value = yesterday.strftime("%Y-%m-%d")
        max_day_value = (yesterday + timedelta(days=14)).strftime("%Y-%m-%d")
        bookings = Booking.objects.filter(patient=patient, booking_date=date, doctor=doctor, time_start=time_start)
        selected_doctor = doctor


        context = {
            'min_day_value': min_day_value,
            'max_day_value': max_day_value,
            'working_hours': working_hours,
            'cat_id': doctor.cat_id,
            'doctors': doctors,
            'appoints': appoints,
            'bookings': bookings,
            'selected_doctor' : selected_doctor,
        }
        return render(request, 'mq/confirm_booking.html', context)
    else:
        return HttpResponseNotAllowed(['POST'])

# Функция для отмены бронирования
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('account')

