from django.contrib import admin

from mailing.models import Mailing, Client, Message


# Register your models here.

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'period', 'start_time', 'stop_time',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'comment',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('theme', 'message')