# Generated by Django 4.1.3 on 2022-12-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_end',
            field=models.DateField(blank=True, null=True, verbose_name='Дата Окончания'),
        ),
    ]
