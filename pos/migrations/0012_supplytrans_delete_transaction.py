# Generated by Django 4.2.6 on 2023-10-30 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0011_remove_employeeprofile_employee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='supplyTrans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='pos.product')),
                ('reciver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_in', to='pos.place')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_out', to='pos.place')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='transaction',
        ),
    ]