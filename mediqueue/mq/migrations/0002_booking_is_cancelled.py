# Generated by Django 4.2.11 on 2024-04-19 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
