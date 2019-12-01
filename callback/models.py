from django.db import models



class CallbackOrder(models.Model):
    userName = models.CharField('Имя',max_length=255, blank=False, default='Нет данных')
    userPhone = models.CharField('Телефон', max_length=255, blank=False, default='Нет данных')
    created_at = models.DateTimeField('Дата заполнения', auto_now_add=True)


    def __str__(self):
        return 'Форма заказа звонка. От {} '.format(self.userName)



    class Meta:
        verbose_name = "Форма заказа звонка"
        verbose_name_plural = "Формы заказа звонка"

class Quiz(models.Model):
    userName = models.CharField('Имя', max_length=255, blank=True, null=True, default='Нет данных')
    userPhone = models.CharField('Телефон', max_length=255, blank=True, null=True, default='Нет данных')
    question1 = models.CharField('Обслуживались ли Вы ранее у сторонней бухгалтерии?',
                                 max_length=255, blank=True, null=True, default='Нет ответа')
    question2 = models.CharField('Количество штатных единиц?', max_length=255, blank=True, null=True,
                                 default='Нет ответа')
    question3 = models.CharField('Количество операций ?', max_length=255, blank=True, null=True,
                                 default='Нет ответа')
    question4 = models.CharField('Система налогообложения?', max_length=255, blank=True, null=True,
                                 default='Нет ответа')
    question5 = models.CharField('Количество контрагентов?', max_length=255, blank=True, null=True,
                                 default='Нет ответа')
    created_at = models.DateTimeField('Дата заполнения', auto_now_add=True)
    is_done = models.BooleanField('Форма обработана? ', default=False)

    def __str__(self):
        return 'Квиз форма. Дата заполнения {} '.format(self.created_at)

    class Meta:
        verbose_name = "Квиз форма"
        verbose_name_plural = "Квиз формы"