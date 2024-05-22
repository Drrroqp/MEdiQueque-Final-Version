from django.contrib.auth.models import User
from django.db import models

# Модель врачей из БД
class Doctors(models.Model):
    title = models.CharField(max_length=45, verbose_name='ФИО врача')
    content = models.TextField(blank=True, verbose_name='Биография')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null = True, verbose_name='Специальность')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Врачи'
        verbose_name_plural = 'Врачи'
        ordering = ['cat', 'title']

# Модель специальностей из БД
class Category(models.Model):
    name = models.TextField(max_length=55, db_index=True, verbose_name='Специальности')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Специальности'
        verbose_name_plural = 'Специальности'
        ordering = ['id', 'name']

# Модель пользователей из БД
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пациент')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    birth_date = models.DateField(verbose_name='Дата рождения')
    email_verified = models.BooleanField(default=False, verbose_name='Почта подтверждена')
    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.user.username if self.user else ""
    def save(self, *args, **kwargs):
        if not self.pk:
            # Если объект UserProfile создается впервые,
            # создаем связанный объект User, если его нет
            if not self.user_id:
                self.user = User.objects.create_user(username=self.phone_number, password='default_password')
        super().save(*args, **kwargs)

# Модель записей из БД
class Booking(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пациент')
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name='Врач')
    booking_date = models.DateField(verbose_name='Дата записи')
    time_start = models.TimeField(verbose_name='Время записи')
    is_cancelled = models.BooleanField(default=False, verbose_name='Отмена записи')

    class Meta:
        verbose_name = 'Записи'
        verbose_name_plural = 'Записи'
        unique_together = ('patient', 'doctor', 'booking_date', 'time_start')

    def __str__(self):
        return f"{self.patient.username} - {self.doctor.title} - {self.booking_date} {self.time_start} - {self.is_cancelled}"


