from datetime import timezone, timedelta
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.utils import timezone
from .models import Booking

# Функция уведомлений за день
@receiver(post_save, sender=Booking)
def email_remind_day(sender, instance, created, **kwargs):
    reminder_date = instance.booking_date - timedelta(days=1)
    if created:
        today = timezone.now().date()
        if reminder_date == today:
            booking_date = instance.booking_date
            time_start = instance.time_start
            patient = instance.patient
            doctor = instance.doctor

            if patient.email:
                patient_email = patient.email
                subject = 'Напоминание: Ваша запись на завтра'
                message = render_to_string('mq/reminder_email.html', {
                    'patient': patient,
                    'doctor': doctor,
                    'booking_date': booking_date,
                    'time_start': time_start,
                })
                send_mail(subject, message, 'mediqueueallow@gmail.com', [patient_email])

# Функция уведомлений после записи
@receiver(post_save, sender=Booking)
def email_remind(sender, instance, created, **kwargs):

    if created:
        booking_date = instance.booking_date
        time_start = instance.time_start
        patient = instance.patient
        doctor = instance.doctor

        if patient.email:
            patient_email = patient.email
            subject = 'Ваша запись'
            message = render_to_string('mq/reminder_email.html', {
                'patient': patient,
                'doctor': doctor,
                'booking_date': booking_date,
                'time_start': time_start,
            })
            send_mail(subject, message, 'mediqueueallow@gmail.com', [patient_email])