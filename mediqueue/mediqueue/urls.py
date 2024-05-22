"""
URL configuration for mediqueue project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from mediqueue import settings
from mq import views
from mq.views import *
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'home'),
    path('login/', cache_page(60*15)(LoginUser.as_view()), name='login'),
    path('logout/', logout_user, name='logout'),
    path('registration/', cache_page(60*15)(RegisterUser.as_view()), name='registration'),
    path('account/', account, name = "account"),
    path('specialities/', cache_page(60*15)(spec_list), name='specialities'),
    path('confirm-booking/', confirm_booking, name='confirm_booking'),
    path('booking/<int:cat_id>/', booking, name='booking'),
    path('cancel_booking/<int:booking_id>/', cancel_booking, name='cancel_booking'),
    path('registration/', cache_page(60*15)(RegisterUser.as_view()), name='registration'),
    path('confirm_email/', cache_page(60*15)(TemplateView.as_view(template_name = 'mq/confirm_email.html')), name = 'confirm_email'),
    path('verify_email/<str:uidb64>/<str:token>', cache_page(60*15)(EmailVerify.as_view()), name = 'verify_email'),
    path('send_verification_email/', cache_page(60*15)(SendVerificationEmail.as_view()), name='send_verification_email'),
    path('invalid_verify/', cache_page(60*15)(TemplateView.as_view(template_name = 'mq/invalid_verify.html')), name='invalid_verify'),
    path('password-reset/', cache_page(60*15)(PasswordResetView.as_view(template_name='mq/password_reset_form.html',
                                                      email_template_name='mq/password_reset_email.html',
                                                      success_url=reverse_lazy('password_reset_done'))), name = 'password_reset'),
    path('password-reset/done', cache_page(60*15)(PasswordResetDoneView.as_view(template_name='mq/password_reset_done.html')), name = 'password_reset_done'),
    path('password-reset/<str:uidb64>/<str:token>', cache_page(60*15)(PasswordResetConfirmView.as_view(template_name='mq/password_reset_confirm.html',
                                                                              success_url=reverse_lazy('password_reset_complete'))), name = 'password_reset_confirm'),
    path('password-reset/complete/', cache_page(60*15)(PasswordResetCompleteView.as_view(template_name='mq/password_reset_complete.html')), name = 'password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
