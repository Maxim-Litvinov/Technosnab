# Generated by Django 3.0.4 on 2020-04-28 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0011_auto_20200429_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='passport_issued',
            field=models.CharField(max_length=100, verbose_name='Паспорт выдан'),
        ),
    ]
