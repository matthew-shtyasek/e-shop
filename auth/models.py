from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.db import models


# CustomUser.objects
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, *args, **kwargs):  # для создания пользователя
        if not email or not password:
            raise ValueError('Email или password являются None!')
        if 'username' not in kwargs.keys():
            raise ValueError('Username должен быть задан!')

        user = CustomUser(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user



class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=128,
                              unique=True,
                              db_index=True,
                              blank=False)
    is_active = models.BooleanField(blank=False,
                                    default=False)
    last_entry_date = models.DateTimeField(auto_now=True)
