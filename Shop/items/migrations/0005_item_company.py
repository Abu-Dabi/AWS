# Generated by Django 4.2.5 on 2023-10-31 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.company'),
        ),
    ]
