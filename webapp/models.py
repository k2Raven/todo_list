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

    def __str__(self):
        return f'{self.id}. {self.title}'
