# Generated by Django 3.0.4 on 2020-03-31 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20200331_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сustomer',
            name='T_customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.Type_customer', verbose_name='Тип заказчика'),
        ),
    ]