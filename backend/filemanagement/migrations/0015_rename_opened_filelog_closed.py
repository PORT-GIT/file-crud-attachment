# Generated by Django 5.1.1 on 2024-09-20 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filemanagement', '0014_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filelog',
            old_name='opened',
            new_name='closed',
        ),
    ]
