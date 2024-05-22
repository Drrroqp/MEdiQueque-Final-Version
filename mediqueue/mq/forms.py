from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from mq.models import UserProfile

# Форма для регистрации
class RegisterUserForm(UserCreationForm):
    # Определение полей формы с указанием виджетов и атрибутов
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Введите логин"}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Введите Имя"}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Введите фамилию"}))
    email = forms.EmailField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Введите почту"}))
    phone_number = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите номер телефона'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': "Введите пароль"}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': "Повторите пароль"}))
    birth_date = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date', 'placeholder': "дд.мм.гггг"}))

    # Методы clean для валидации полей
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not phone_number.startswith(('8', '7')) or len(phone_number) != 11:
            raise ValidationError('Неправильный формат номера телефона.')
        return phone_number

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha() or not first_name[0].isupper():
            raise ValidationError('Неправильный формат имени.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha() or not last_name[0].isupper():
            raise ValidationError('Неправильный формат фамилии.')
        return last_name

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'phone_number', 'password1', 'password2',  'birth_date')

    # Метод для сохранения данных формы в базу данных
    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            profile = UserProfile.objects.create(user=user, phone_number=self.cleaned_data['phone_number'],
                                                 birth_date=self.cleaned_data['birth_date'])
            profile.save()  # Сохраняем профиль
        return user

# Форма для аунтификации
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Введите логин"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': "Введите пароль"}))

    class Meta:
        fields = ('username', 'password')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user_profile = UserProfile.objects.get(user__username=username)
                if not user_profile.email_verified:
                    raise forms.ValidationError("Почта не подтверждена.")
            except UserProfile.DoesNotExist:
                raise forms.ValidationError("Неправильное имя пользователя или пароль.")

        return cleaned_data

# Форма для сброса пароля
class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email')
class CustomPasswordResetForm(PasswordResetForm):
    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=None, from_email=None,
             request=None, html_email_template_name=None, extra_email_context=None):
        email = self.cleaned_data["email"]
        # Проверяем существование пользователя с указанным email в базе данных
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError("Пользователь с указанным email не найден.")
        super().save(domain_override=domain_override, subject_template_name=subject_template_name,
                     email_template_name=email_template_name, use_https=use_https,
                     token_generator=token_generator, from_email=from_email, request=request,
                     html_email_template_name=html_email_template_name, extra_email_context=extra_email_context)