# Generated by Django 5.1.1 on 2024-09-17 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filemanagement', '0003_remove_filelog_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filemovement',
            name='left_at',
        ),
        migrations.RemoveField(
            model_name='filemovement',
            name='moved_at',
        ),
    ]
