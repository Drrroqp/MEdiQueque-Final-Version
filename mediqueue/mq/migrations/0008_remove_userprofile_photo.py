# Generated by Django 4.2.11 on 2024-04-28 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mq', '0007_userprofile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='photo',
        ),
    ]
