# Generated by Django 5.1.1 on 2024-09-17 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filemanagement', '0004_remove_filemovement_left_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filemovement',
            name='movement',
        ),
        migrations.DeleteModel(
            name='Filelog',
        ),
        migrations.DeleteModel(
            name='Filemovement',
        ),
    ]
