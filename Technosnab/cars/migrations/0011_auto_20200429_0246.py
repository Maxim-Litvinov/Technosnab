# Generated by Django 3.0.4 on 2020-04-28 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_repairs_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'ordering': ['state_number'], 'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
    ]