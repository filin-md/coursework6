from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {'null': True, 'blank': True}


# Create your models here.


class Message(models.Model):
    theme = models.CharField(max_length=150, verbose_name='Тема письма')
    message = models.TextField(verbose_name='Текст письма')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец')


    def __str__(self):
        return f'{self.theme}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Client(models.Model):
    email = models.EmailField(verbose_name='email', unique=True, )
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец')


    def __str__(self):
        return f'{self.full_name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Кллиенты'


class Mailing(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
        (PERIOD_MONTHLY, 'Раз в месяц'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'
    STATUSES = (
        (STATUS_STARTED, 'Запущена'),
        (STATUS_CREATED, 'Создана'),
        (STATUS_DONE, 'Завершена'),
    )

    start_time = models.DateTimeField(default=timezone.now, verbose_name='Дата начала рассылки')
    stop_time = models.DateTimeField(verbose_name='Дата окончания рассылки')
    status = models.CharField(max_length=20, choices=STATUSES, default=STATUS_CREATED, verbose_name='Статус рассылки')
    period = models.CharField(max_length=20, choices=PERIODS, default=PERIOD_DAILY,
                              verbose_name='Периодичность рассылки')

    mail_to = models.ManyToManyField(Client, verbose_name='Кому')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение', **NULLABLE)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец')

    def __str__(self):
        return f'{self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class MailingLog(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'
    STATUSES = (
        (STATUS_OK, 'Успешно'),
        (STATUS_FAILED, 'Ошибка'),
    )

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    status = models.CharField(choices=STATUSES, default=STATUS_OK, verbose_name='Статус')
    last_try = models.DateTimeField(auto_now_add=True, verbose_name='Дата последней попытки')

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
