# Generated by Django 4.2.6 on 2023-10-29 12:21

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0005_alter_employeeprofile_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubManager',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pos.user',),
            managers=[
                ('submanger', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_work_at', to='pos.place'),
        ),
    ]
