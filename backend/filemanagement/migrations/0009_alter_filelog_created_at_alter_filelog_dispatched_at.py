# Generated by Django 5.1.1 on 2024-09-18 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanagement', '0008_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filelog',
            name='created_at',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='filelog',
            name='dispatched_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
