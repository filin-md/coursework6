
from django.db import models
from django.utils import timezone

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Article(models.Model):

    title = models.CharField(verbose_name='заголовок')
    text = models.TextField(verbose_name='содержимое статьи')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    views_count = models.PositiveIntegerField(verbose_name='количество просмотров', default=0)
    create_date = models.DateTimeField(default=timezone.now, verbose_name='дата создания')
