# Generated by Django 3.1.5 on 2021-01-26 21:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20210125_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybook',
            name='date_from',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='propertybook',
            name='date_to',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]