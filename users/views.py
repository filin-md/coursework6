import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserUpdateForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message=f"Вы успешно зарегистрировались. Осталось подтвердить вашу учётную запись"
                    f"Код подтверждения - {new_user.token}"
                    f"Перейдите по ссылке и введите его в поле ввода. {reverse_lazy('users:confirmation')}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]

        )
        return super().form_valid(form)

class UserUpdateView(UpdateView):
    model = User
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:profile')
    form_class = UserUpdateForm

    def get_object(self, queryset=None):
        return self.request.user

def generate_new_password(request):

    new_password = ''.join([str(random.randint(0,9)) for _ in range(12)])
    request.user.set_password(new_password)
    request.user.save()
    send_mail(
        subject='Пароль изменён',
        message=f'Вы успешно изменили пароль! Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]

    )

    return redirect(reverse('home'))

def confirmation(request):
    request.user.is_active = True