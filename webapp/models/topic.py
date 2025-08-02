from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название', null=False, blank=False)
    description = models.TextField(verbose_name='Описание', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               verbose_name='Автор', related_name='topics')
    comments = models.PositiveIntegerField(default=0, verbose_name="Комментарии")

    def __str__(self):
        return f"{self.id} | {self.name} | {self.created_at} "

    class Meta:
        db_table = 'topics'
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def get_absolute_url(self):
        return reverse('webapp:topic_detail', kwargs={'pk': self.pk})