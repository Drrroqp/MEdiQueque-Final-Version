from datetime import datetime
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

admin.site.site_header = "Административная панель MediQueue"
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat')
    search_fields = ('title', 'cat')
    list_display_links = ('title', 'cat')

admin.site.register(Doctors, DoctorsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'id')
    list_display_links = ('id', 'name')

admin.site.register(Category, CategoryAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone_number', 'birth_date',)

    def full_name(self, obj):
        return obj.user.get_full_name() if obj.user.get_full_name() else obj.user.username
    full_name.short_description = 'Пациент'

    def email(self, obj):
        return obj.user.email
    email.short_description = 'Почта'

    def phone_number(self, obj):
        return obj.phone_number
    phone_number.short_description = 'Номер телефона'

    def birth_date(self, obj):
        return obj.birth_date
    birth_date.short_description = 'Дата рождения'


admin.site.register(UserProfile, UserProfileAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking_date', 'time_start', 'doctor', 'patient', 'is_cancelled')
    list_filter = ('is_cancelled',)
    search_fields = ('id', 'booking_date', 'time_start', 'doctor', 'patient', 'is_cancelled')
    list_display_links = ('id', 'booking_date', 'time_start', 'doctor', 'patient', 'is_cancelled')

admin.site.register(Booking, BookingAdmin)