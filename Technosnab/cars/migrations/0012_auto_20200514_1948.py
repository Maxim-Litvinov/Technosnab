# Generated by Django 3.0.4 on 2020-05-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_auto_20200429_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='state_number',
            field=models.CharField(max_length=7, unique=True, verbose_name='Гос номер'),
        ),
    ]
