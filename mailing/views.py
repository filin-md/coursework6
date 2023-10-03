from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from mailing.models import Client, Mailing, Message


# Create your views here.


def index(request):
    return render(request, 'mailing/base.html')


class ClientCreateView(CreateView):
    model = Client
    fields = 'email', 'full_name', 'comment'
    success_url = reverse_lazy('mailing:clients')


class ClientListView(ListView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = 'email', 'full_name', 'comment'
    success_url = reverse_lazy('mailing:clients')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients')


class ClientDetailView(DetailView):
    model = Client
    template_name = 'mailing/client.html'


class MailingCreateView(CreateView):
    model = Mailing
    fields = 'start_time', 'stop_time', 'period', 'mail_to', 'message'
    success_url = reverse_lazy('mailing:mailings')


class MailingListView(ListView):
    model = Mailing


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = 'start_time', 'stop_time', 'period', 'mail_to', 'message'
    success_url = reverse_lazy('mailing:mailings')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailings')


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing/mailing.html'


class MessageCreateView(CreateView):
    model = Message
    fields = 'theme', 'message'
    success_url = reverse_lazy('mailing:messages')


class MessageListView(ListView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    fields = 'theme', 'message'
    success_url = reverse_lazy('mailing:messages')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:messages')


class MessageDetailView(DetailView):
    model = Message
    template_name = 'mailing/message.html'
