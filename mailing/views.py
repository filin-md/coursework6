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

    def form_valid(self, form):
        client = form.save(commit=False)
        client.owner = self.request.user
        client.save()
        return super().form_valid(form)


class ClientListView(ListView):
    model = Client

    def get_queryset(self):
        queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset


class ClientUpdateView(UpdateView):
    model = Client
    fields = 'email', 'full_name', 'comment'
    success_url = reverse_lazy('mailing:clients')

    def get_queryset(self):
        queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients')

    def get_queryset(self):
        queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset


class ClientDetailView(DetailView):
    model = Client
    template_name = 'mailing/client.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset


class MailingCreateView(CreateView):
    model = Mailing
    fields = 'start_time', 'stop_time', 'period', 'mail_to', 'message'
    success_url = reverse_lazy('mailing:mailings')

    def form_valid(self, form):
        mailing = form.save(commit=False)
        mailing.owner = self.request.user
        mailing.save()
        return super().form_valid(form)




class MailingListView(ListView):
    model = Mailing

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.groups.filter(name='manager').exists():
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = 'start_time', 'stop_time', 'period', 'mail_to', 'message'
    success_url = reverse_lazy('mailing:mailings')

    def get_queryset(self):
        queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailings')

    def get_queryset(self):
        queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing/mailing.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset


class MessageCreateView(CreateView):
    model = Message
    fields = 'theme', 'message'
    success_url = reverse_lazy('mailing:messages')

    def form_valid(self, form):
        message = form.save(commit=False)
        message.owner = self.request.user
        message.save()
        return super().form_valid(form)


class MessageListView(ListView):
    model = Message

    def get_queryset(self):
        queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset


class MessageUpdateView(UpdateView):
    model = Message
    fields = 'theme', 'message'
    success_url = reverse_lazy('mailing:messages')

    def get_queryset(self):
        queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:messages')

    def get_queryset(self):
        queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset


class MessageDetailView(DetailView):
    model = Message
    template_name = 'mailing/message.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset
