from django.contrib.auth import get_user_model
from django.db import models

from webapp.models import Topic


class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topic_comments', verbose_name='Тема')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               verbose_name='Автор', related_name='comments')
    content = models.TextField(verbose_name="Комментарий", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")


    def __str__(self):
        return f"{self.author} | {self.content[:30]} | {self.created_at} "

    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
