from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    """Модель задачи, создаваемой пользователем"""
    title = models.CharField(max_length=100, verbose_name='Название')
    memo = models.TextField(blank=True, verbose_name='Описание')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_completed = models.DateTimeField(null=True, verbose_name='Дата выполнения', blank=True)
    is_important = models.BooleanField(default=False, verbose_name='Пометить как важное')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
