import os
import django
from pathlib import Path

from django.core.mail import send_mail

from django.conf import settings


def send_email_periodically():
    print(settings.EMAIL_HOST_USER)
    mail = send_mail(
        'theme',
        'body',
        settings.EMAIL_HOST_USER,
        ['filin.work@ya.ru'],
        fail_silently=False,
    )
    print(mail)