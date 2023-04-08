from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from auth.forms import CustomUserRegister
from auth.models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserRegister
    template_name = 'auth/register.html'
    success_url = reverse_lazy('cat:list')

    def post(self, request, *args, **kwargs):
        if self.form_class(request.POST).is_valid():
            message = render(request, 'auth/vefiry_register.html')
            send_mail(subject='Регистрация на сайте лучшего интернет-магазина',
                      message='Для подтверждения перейдите по ссылке',
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[request.POST.get('email')])

        result = super().post(request, *args, **kwargs)
        return result
