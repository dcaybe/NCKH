# Generated by Django 5.1.6 on 2025-05-20 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_nckh9', '0005_infostudent_khoahoc'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinhvientdg',
            name='trangthai',
            field=models.BooleanField(default=False),
        ),
    ]
