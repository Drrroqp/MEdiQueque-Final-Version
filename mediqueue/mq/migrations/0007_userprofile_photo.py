# Generated by Django 4.2.11 on 2024-04-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mq', '0006_alter_booking_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
