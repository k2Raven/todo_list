# Generated by Django 4.1.3 on 2022-11-26 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_task_type_old'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='webapp.type'),
        ),
    ]
