# Generated by Django 3.1.5 on 2021-01-19 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='settings/')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=224)),
                ('description', models.TextField(max_length=300)),
                ('fb_link', models.URLField()),
                ('tw_link', models.URLField()),
                ('ins_link', models.URLField()),
            ],
        ),
    ]
