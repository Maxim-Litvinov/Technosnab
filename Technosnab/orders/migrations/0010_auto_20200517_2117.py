# Generated by Django 3.0.4 on 2020-05-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20200509_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата'),
        ),
    ]