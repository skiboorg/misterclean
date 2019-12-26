# Generated by Django 2.2.7 on 2019-12-26 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20191226_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(null=True, upload_to='services_img/', verbose_name='Иконка')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.ServiceName', verbose_name='Фото работ для услуги')),
            ],
            options={
                'verbose_name': 'Фото работ для услуги',
                'verbose_name_plural': 'Фото работ для услуги',
            },
        ),
    ]
