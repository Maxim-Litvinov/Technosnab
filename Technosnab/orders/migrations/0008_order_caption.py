# Generated by Django 3.0.4 on 2020-05-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200429_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='caption',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Примечание'),
        ),
    ]
