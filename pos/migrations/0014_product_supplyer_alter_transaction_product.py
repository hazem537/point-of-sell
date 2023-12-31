# Generated by Django 4.2.6 on 2023-10-30 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0013_rename_supplytrans_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='supplyer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='pos.supplyer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trans', to='pos.product'),
        ),
    ]
