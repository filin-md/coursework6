from django.urls import path

from mailing.views import index, ClientCreateView, ClientListView, ClientUpdateView, ClientDeleteView, ClientDetailView, \
    MailingListView, MailingCreateView, MailingUpdateView, MailingDeleteView, MailingDetailView, MessageListView, \
    MessageCreateView, MessageDeleteView, MessageDetailView, MessageUpdateView

app_name = 'mailing'


urlpatterns = [
    path('', index, name='home'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),
    path('clients/<int:pk>', ClientDetailView.as_view(), name='client'),

    path('mailings/', MailingListView.as_view(), name='mailings'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('update_mailing/<int:pk>', MailingUpdateView.as_view(), name='update_mailing'),
    path('delete_mailing/<int:pk>', MailingDeleteView.as_view(), name='delete_mailing'),
    path('mailings/<int:pk>', MailingDetailView.as_view(), name='mailing'),

    path('messages/', MessageListView.as_view(), name='messages'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('update_message/<int:pk>', MessageUpdateView.as_view(), name='update_message'),
    path('delete_message/<int:pk>', MessageDeleteView.as_view(), name='delete_message'),
    path('messages/<int:pk>', MessageDetailView.as_view(), name='message')
]
