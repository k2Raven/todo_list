from django.contrib.auth import get_user_model
from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=40, verbose_name="Тип")

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=40, verbose_name="Статус")

    def __str__(self):
        return self.name


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey('webapp.Status', related_name='tasks', on_delete=models.PROTECT, verbose_name='Статус')
    types = models.ManyToManyField('webapp.Type', related_name='tasks', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    project = models.ForeignKey('webapp.Project', related_name='tasks', on_delete=models.CASCADE, verbose_name='Проект')

    def __str__(self):
        return f'{self.id}. {self.title}'


class Project(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название')
    description = models.TextField(max_length=3000, verbose_name='Описание')
    date_started = models.DateField(verbose_name='Дата Начала')
    date_end = models.DateField(null=True, blank=True, verbose_name='Дата Окончания')
    is_deleted = models.BooleanField(default=False)
    users = models.ManyToManyField(get_user_model(), related_name='projects', blank=True, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.id}. {self.title}'
