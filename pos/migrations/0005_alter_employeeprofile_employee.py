# Generated by Django 4.2.6 on 2023-10-29 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0004_alter_employeeprofile_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='pos.employee'),
        ),
    ]
