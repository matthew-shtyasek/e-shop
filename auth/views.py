from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from auth.forms import CustomUserRegister
from auth.models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserRegister
    template_name = 'auth/register.html'
    success_url = reverse_lazy('cat:list')

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        '''from django.core.mail import send_mail'''
        '''from django.conf import settings'''
        message = render(request, 'auth/vefiry_register.html')
        send_mail(subject='Регистрация на сайте лучшего интернет-магазина',
                  html_message=message,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[request.POST.get('email')])
        return result
