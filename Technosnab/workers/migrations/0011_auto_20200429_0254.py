# Generated by Django 3.0.4 on 2020-04-28 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0010_auto_20200429_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='passport_number',
            field=models.CharField(max_length=6, unique=True, verbose_name='Номер Паспорта'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='passport_seria',
            field=models.CharField(max_length=4, unique=True, verbose_name='Серия Паспорта'),
        ),
    ]