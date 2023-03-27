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
        return result
