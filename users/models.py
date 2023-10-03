from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна')

    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='mailing_users_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True,
                                              related_name='mailing_users_permissions')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


