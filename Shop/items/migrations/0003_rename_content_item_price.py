# Generated by Django 4.2.5 on 2023-09-27 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_item_image_alter_itemimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='content',
            new_name='price',
        ),
    ]
