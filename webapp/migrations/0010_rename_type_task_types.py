# Generated by Django 4.1.3 on 2022-11-26 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_remove_task_type_old'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='type',
            new_name='types',
        ),
    ]