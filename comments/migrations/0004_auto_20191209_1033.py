# Generated by Django 2.2.7 on 2019-12-09 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20191205_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='writtenByAvatar',
            field=models.ImageField(null=True, upload_to='comments', verbose_name='Аватарка кто оставил отзыв 115x115'),
        ),
    ]
