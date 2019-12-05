# Generated by Django 2.2.7 on 2019-12-05 16:10

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20191130_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seotag',
            name='postsDescription',
        ),
        migrations.RemoveField(
            model_name='seotag',
            name='postsKeywords',
        ),
        migrations.RemoveField(
            model_name='seotag',
            name='postsTitle',
        ),
        migrations.RemoveField(
            model_name='servicename',
            name='bottomText',
        ),
        migrations.RemoveField(
            model_name='servicename',
            name='pageTable',
        ),
        migrations.RemoveField(
            model_name='servicename',
            name='topText',
        ),
        migrations.AddField(
            model_name='seotag',
            name='contactDescription',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег Description для страницы контакты '),
        ),
        migrations.AddField(
            model_name='seotag',
            name='contactKeywords',
            field=models.TextField(blank=True, null=True, verbose_name='Тег Keywords для страницы контакты'),
        ),
        migrations.AddField(
            model_name='seotag',
            name='contactTitle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег Title для страницы контакты'),
        ),
        migrations.AddField(
            model_name='servicename',
            name='pageText',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст на страницу с услугой'),
        ),
        migrations.AddField(
            model_name='servicename',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Стоимость услуги'),
        ),
    ]
