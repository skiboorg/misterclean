# Generated by Django 2.2.7 on 2020-01-15 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20191227_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicename',
            name='order',
            field=models.IntegerField(default=1, verbose_name='Порядковый номер'),
        ),
    ]
