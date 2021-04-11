# Generated by Django 3.0.4 on 2020-05-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_auto_20200514_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='cost',
            field=models.IntegerField(default=0, null=True, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='description',
            field=models.CharField(default='-', max_length=400, null=True, verbose_name='Описание затраты'),
        ),
        migrations.AlterField(
            model_name='repairs_type',
            name='description',
            field=models.CharField(max_length=400, verbose_name='Наименование типа ремонта'),
        ),
    ]