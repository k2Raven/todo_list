from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название')
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0],
                              verbose_name='Статус')
    deadline = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return f'{self.id}. {self.title}'