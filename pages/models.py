from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from random import choices
import string

class ServiceName(models.Model):
    name = models.CharField('Вид работы', max_length=255, blank=False, null=True)
    image = models.ImageField('Изображение для страницы со всеми услугами (555 x 225)', upload_to='services_img/', blank=True, null=True)
    image_small = models.ImageField('Изображение для главной превью (170 x 170)', upload_to='services_img/', blank=True, null=True)
    name_lower = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, unique=True, db_index=True)
    page_h1 = models.CharField('Тег H1', max_length=255, blank=False, null=True)
    page_title = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True)
    page_description = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True)
    page_keywords = models.TextField('Keywords SEO', blank=True, null=True)
    price = models.IntegerField('Стоимость услуги без скидки', default=0)
    price1 = models.IntegerField('Скидка свыше 50 кв.м.', default=0)
    price2 = models.IntegerField('Скидка свыше 100 кв.м.', default=0)
    pageText = RichTextUploadingField('Текст на страницу с услугой', blank=True, null=True)
    isAtHome = models.BooleanField('Отображать на главной?', default=False)
    isInCalc = models.BooleanField('Отображать в калькуляторе?', default=False)


    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if self.name_slug != slug:
            testSlug = ServiceName.objects.filter(name_slug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.name_slug = slug + slugRandom
        self.name_lower = self.name.lower()
        super(ServiceName, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return '/service/{}/'.format(self.name_slug)

    def __str__(self):
        return 'Вид работы : {}'.format(self.name)

    class Meta:
        verbose_name = "Вид работы"
        verbose_name_plural = "Виды работ"



class SeoTag(models.Model):
    indexTitle = models.CharField('Тег Title для главной', max_length=255, blank=True, null=True)
    indexDescription = models.CharField('Тег Description для главной', max_length=255, blank=True, null=True)
    indexKeywords = models.TextField('Тег Keywords для главной',  blank=True, null=True)
    servicesTitle = models.CharField('Тег Title для страницы со всеми услугами', max_length=255, blank=True, null=True)
    servicesDescription = models.CharField('Тег Description для страницы со всеми услугам', max_length=255, blank=True, null=True)
    servicesKeywords = models.TextField('Тег Keywords для страницы со всеми услугам', blank=True, null=True)
    # postsTitle = models.CharField('Тег Title для страницы со всеми статьями', max_length=255, blank=True, null=True)
    # postsDescription = models.CharField('Тег Description для страницы со всеми статьями', max_length=255, blank=True,
    #                                        null=True)
    # postsKeywords = models.TextField('Тег Keywords для страницы со всеми статьями', blank=True, null=True)
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


