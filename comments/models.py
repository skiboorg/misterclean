from django.db import models
from pages.models import ServiceName

class Comment(models.Model):
    service = models.ManyToManyField(ServiceName,verbose_name='Отзыв к услуге')
    image = models.ImageField('Картинка отзыва большая 750 х 390 px', upload_to='comments', blank=False)
    writtenBy = models.CharField('От кого отзыв', max_length=75, blank=False, default='')
    writtenByAvatar = models.ImageField('Аватарка кто оставил отзыв 115x115', upload_to='comments', blank=False, null=True)
    writtenByVk = models.CharField('Ссылка на ВК', max_length=75, blank=False, null=True)
    description = models.TextField('Текст отзыва (примерно 380 слов)',  blank=False, null=True)


    def __str__(self):
        return 'Отзыв №{}'.format(self.id)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class VideoComment(models.Model):
    service = models.ManyToManyField(ServiceName,verbose_name='Видео отзыв к услуге')
    url = models.CharField('youtube-video-id', max_length=75, blank=False, null=True)



    def __str__(self):
        return 'Видео отзыв №{}'.format(self.id)

    class Meta:
        verbose_name = "Видео отзыв"
        verbose_name_plural = "Видео отзывы"