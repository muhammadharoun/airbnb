# Generated by Django 3.1.5 on 2021-01-25 00:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20210125_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybook',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
