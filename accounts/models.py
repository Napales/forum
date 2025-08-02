from django.contrib.auth.models import AbstractUser
from django.db import models


def upload_to(instance, filename):
    return f'avatars/{instance.username}/{filename}'

class MyUser(AbstractUser):
    avatar = models.ImageField(upload_to=upload_to, verbose_name='Аватар', blank=False, null=False)
    comments_count = models.PositiveIntegerField(default=0, verbose_name="Количество комментариев")