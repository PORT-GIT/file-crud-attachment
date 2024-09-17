# Generated by Django 5.1.1 on 2024-09-17 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filelog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(choices=[('CHOOSE DEPARTMENT', 'Choose Department'), ('ADM', 'Administration'), ('HR', 'Human Resources'), ('PUB', 'Publicity & Communications'), ('PROC', 'Procurement'), ('PRM', 'Property Management'), ('CBN', 'Claims & Benefits'), ('HSP', 'Hospitals'), ('MEM', 'Membership'), ('LEG', 'Legal'), ('TRS', 'Transport'), ('REP', 'Reports'), ('ST', 'Standards'), ('FIN', 'Finance'), ('C', 'Confidential')], default='CHOOSE DEPARTMENT', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('basic_holder', models.CharField(default='Central Registry', max_length=50)),
                ('type', models.CharField(choices=[('File', 'F'), ('Box File', 'BF')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Filemovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moved_at', models.DateTimeField(auto_now_add=True)),
                ('left_at', models.DateTimeField()),
                ('current_holder', models.CharField(max_length=200)),
                ('movement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filemanagement.filelog')),
            ],
        ),
    ]
