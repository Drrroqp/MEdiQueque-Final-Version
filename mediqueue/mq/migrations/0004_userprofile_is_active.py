# Generated by Django 4.2.11 on 2024-04-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mq', '0003_alter_booking_options_alter_userprofile_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Ваша почта должна быть подтверждена!'),
        ),
    ]
