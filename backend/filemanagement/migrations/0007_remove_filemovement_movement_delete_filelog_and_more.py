# Generated by Django 5.1.1 on 2024-09-18 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filemanagement', '0006_initial'),
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
