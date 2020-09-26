import os

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from pytils.translit import slugify
from random import choices
from PIL import Image
import string
import uuid

from misterclean.settings import BASE_DIR
import misterclean.settings

class ServiceName(models.Model):
    order = models.IntegerField('Порядковый номер', default=1)
    name = models.CharField('Вид работы', max_length=255, blank=False, null=True)
    image = models.ImageField('Изображение для страницы со всеми услугами (555 x 225)', upload_to='services_img/', blank=True, null=True)
    image_small = models.ImageField('Изображение для главной превью (170 x 170)', upload_to='services_img/', blank=True, null=True)
    image_inner = models.ImageField('Изображение для блока о нас', upload_to='services_img/', blank=True, null=True)
    name_lower = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, unique=True, db_index=True)
    page_h1 = models.CharField('Тег H1', max_length=255, blank=False, null=True)
    page_title = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True)
    page_description = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True)
    page_keywords = models.TextField('Keywords SEO', blank=True, null=True)
    price = models.IntegerField('Стоимость услуги без скидки', default=0)
    price1 = models.IntegerField('Скидка свыше 50 кв.м.', default=0)
    price2 = models.IntegerField('Скидка свыше 100 кв.м.', default=0)
    smallText = RichTextUploadingField('Текст на страницу с услугой (отображается вверху страницы) ', blank=True,
                                      null=True)
    pageText = RichTextUploadingField('Текст на страницу с услугой (отображается внизу страницы) ', blank=True, null=True)
    isAtHome = models.BooleanField('Отображать на главной?', default=False)
    isInCalc = models.BooleanField('Отображать в калькуляторе?', default=False)
    show_calc = models.BooleanField('Отображать калькулятор на странице', default=True)


    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if not self.name_slug:
            testSlug = ServiceName.objects.filter(name_slug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.name_slug = slug + slugRandom
        self.name_lower = self.name.lower()
        super(ServiceName, self).save(*args, **kwargs)

    def get_about_bg(self):
        if self.image_inner:
            return self.image_inner.url
        else:
            return '/static/img/bg2.png'
        
    def get_absolute_url(self):
        return '/service/{}/'.format(self.name_slug)

    def __str__(self):
        return 'Вид работы : {}'.format(self.name)

    class Meta:
        verbose_name = "Вид работы"
        verbose_name_plural = "Виды работ"

class ServicePrice(models.Model):
    service = models.ForeignKey(ServiceName,blank=False,null=True,on_delete=models.CASCADE,verbose_name='Разновидность услуги')
    name = models.CharField('Название разновидности услуги', max_length=255, blank=False, null=True)
    info = models.CharField('Описание разновидности услуги', max_length=255, blank=True, null=True)
    price = models.IntegerField('Стоимость', blank=False, null=True)

    def __str__(self):
        return 'Pазновидность услуги : {}'.format(self.service.name)

    class Meta:
        verbose_name = "Pазновидность услуги"
        verbose_name_plural = "Pазновидности услуг"

class ServiceFeature(models.Model):
    service = models.ForeignKey(ServiceName,blank=False,null=True,on_delete=models.CASCADE,verbose_name='Приемущества для услуги')
    name = models.CharField('Описание приемущества услуги', max_length=255, blank=False, null=True)
    icon = models.ImageField('Иконка', upload_to='services_img/', blank=False, null=True)

    def __str__(self):
        return 'Приемущество услуги : {}'.format(self.service.name)

    class Meta:
        verbose_name = "Приемущество услуги"
        verbose_name_plural = "Приемущества услуг"


class ServiceSteps(models.Model):
    service = models.ForeignKey(ServiceName, blank=False, null=True, on_delete=models.CASCADE,
                                verbose_name='Этапы работ для услуги')
    name = models.CharField('Описание этапа работ', max_length=255, blank=False, null=True)
    icon = models.ImageField('Иконка', upload_to='services_img/', blank=False, null=True)

    def __str__(self):
        return 'Этап работ для услуги : {}'.format(self.service.name)

    class Meta:
        verbose_name = "Этап работ"
        verbose_name_plural = "Этапы работ"

class ServiceImage(models.Model):
    service = models.ForeignKey(ServiceName,blank=False,null=True,on_delete=models.CASCADE,verbose_name='Фото работ для услуги')

    icon = models.ImageField('Фото', upload_to='services_img/', blank=False, null=True)
    image_small = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return 'Фото работ для услуги : {}'.format(self.service.name)

    class Meta:
        verbose_name = "Фото работ для услуги"
        verbose_name_plural = "Фото работ для услуги"
    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        if self.image_small:
            return mark_safe('<img src="{}" width="150" height="150" style="object-fit:cover" />'.format(self.image_small))
        else:
            return mark_safe('<span>НЕТ МИНИАТЮРЫ</span>')

    image_tag.short_description = 'Картинка'

    def save(self, *args, **kwargs):
        fill_color = '#fff'
        image = Image.open(self.icon)


        if image.mode in ('RGBA', 'LA'):
            background = Image.new(image.mode[:-1], image.size, fill_color)
            background.paste(image, image.split()[-1])
            image = background
        image.thumbnail((250, 250), Image.ANTIALIAS)
        small_name = 'media/items/{}/{}'.format(self.service.id, str(uuid.uuid4()) + '.jpg')
        if misterclean.settings.DEBUG:
            os.makedirs('media/items/{}'.format(self.service.id), exist_ok=True)
            image.save(small_name, 'JPEG', quality=90)
        else:
            os.makedirs('C:\inetpub\wwwroot\mc\media\items/{}'.format(self.service.id), exist_ok=True)
            image.save('mc/' + small_name, 'JPEG', quality=90)
        self.image_small = '/' + small_name

        super(ServiceImage, self).save(*args, **kwargs)

class SeoTag(models.Model):
    indexTitle = models.CharField('Тег Title для главной', max_length=255, blank=True, null=True)
    indexDescription = models.CharField('Тег Description для главной', max_length=255, blank=True, null=True)
    indexKeywords = models.TextField('Тег Keywords для главной',  blank=True, null=True)
    servicesTitle = models.CharField('Тег Title для страницы со всеми услугами', max_length=255, blank=True, null=True)
    servicesDescription = models.CharField('Тег Description для страницы со всеми услугам', max_length=255, blank=True, null=True)
    servicesKeywords = models.TextField('Тег Keywords для страницы со всеми услугам', blank=True, null=True)
    postsTitle = models.CharField('Тег Title для страницы со всеми статьями', max_length=255, blank=True, null=True)
    postsDescription = models.CharField('Тег Description для страницы со всеми статьями', max_length=255, blank=True,
                                           null=True)
    postsKeywords = models.TextField('Тег Keywords для страницы со всеми статьями', blank=True, null=True)
    aboutTitle = models.CharField('Тег Title для страницы о компании', max_length=255, blank=True, null=True)
    aboutDescription = models.CharField('Тег Description для страницы о компании', max_length=255, blank=True,
                                        null=True)
    aboutKeywords = models.TextField('Тег Keywords для страницы о компании', blank=True, null=True)
    contactTitle = models.CharField('Тег Title для страницы контакты', max_length=255, blank=True, null=True)
    contactDescription = models.CharField('Тег Description для страницы контакты ', max_length=255, blank=True,
                                        null=True)
    contactKeywords = models.TextField('Тег Keywords для страницы контакты', blank=True, null=True)

    yandexMetrika = models.TextField('Код Яндекс метрики',  blank=True, null=True)
    fbPixel = models.TextField('Код пикселя', blank=True, null=True)
    yandexTAG = models.CharField('Код подтверждения Яндекс', max_length=255, blank=True, null=True)
    googleTAG = models.CharField('Код подтверждения google', max_length=255, blank=True, null=True)


    def __str__(self):
        return 'Теги для статических страниц'

    class Meta:
        verbose_name = "Теги для статических страниц"
        verbose_name_plural = "Теги для статических страниц"


