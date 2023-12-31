# Generated by Django 4.2.6 on 2023-10-29 13:17

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0008_submanagerprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pos.place',),
            managers=[
                ('port', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pos.place',),
            managers=[
                ('store', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='role',
            field=models.CharField(choices=[('STORE', 'Store'), ('PORT', 'Port')], default=None, max_length=50),
            preserve_default=False,
        ),
    ]
