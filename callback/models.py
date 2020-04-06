from django.db import models
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.template.loader import render_to_string
import settings

class CallbackOrder(models.Model):
    userName = models.CharField('Имя',max_length=255, blank=False, default='Нет данных')
    userPhone = models.CharField('Телефон', max_length=255, blank=False, default='Нет данных')
    service = models.CharField('Услуга', max_length=255, blank=True, default='Нет данных')
    square = models.CharField('Площадь', max_length=255, blank=True, default='Нет данных')
    created_at = models.DateTimeField('Дата заполнения', auto_now_add=True)


    def __str__(self):
        return 'Форма заказа звонка. От {} '.format(self.userName)



    class Meta:
        verbose_name = "Форма заказа звонка"
        verbose_name_plural = "Формы заказа звонка"

def callback_ps(sender, instance, **kwargs):
    msg_html = render_to_string('email/callback.html', {'userName': instance.userName,
                                                        'userPhone': instance.userPhone,
                                                        'service': instance.service,
                                                        'square': instance.square,})
    send_mail('Заполнена форма на сайте MisterClean ', None, 'no-reply@specsintez-pro.ru', [settings.SEND_TO],
              fail_silently=False, html_message=msg_html)

post_save.connect(callback_ps, sender=CallbackOrder)