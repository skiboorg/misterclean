# Generated by Django 2.2.7 on 2019-11-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='userName',
            field=models.CharField(default='Нет данных', max_length=255, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='userPhone',
            field=models.CharField(default='Нет данных', max_length=255, verbose_name='Телефон'),
        ),
    ]
