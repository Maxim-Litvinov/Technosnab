# Generated by Django 3.0.4 on 2020-05-26 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0015_auto_20200517_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='passport_img',
            field=models.ImageField(blank=True, null=True, upload_to='pasport_img/', verbose_name='Скан паспорта'),
        ),
    ]
