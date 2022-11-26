# Generated by Django 4.1.3 on 2022-11-26 13:11

from django.db import migrations


def transfer_type(apps, schema_editor):
    Task = apps.get_model('webapp.Task')
    for task in Task.objects.all():
        task.type.add(task.type_old)


def rollback_transfer(apps, schema_editor):
    Task = apps.get_model('webapp.Task')
    for task in Task.objects.all():
        type = task.type.first()
        if type:
            task.type_old = type


class Migration(migrations.Migration):
    dependencies = [
        ('webapp', '0007_task_type'),
    ]

    operations = [
        migrations.RunPython(transfer_type, rollback_transfer)
    ]
