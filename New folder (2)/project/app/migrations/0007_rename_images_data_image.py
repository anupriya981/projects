# Generated by Django 5.0.2 on 2024-07-26 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_data_age_data_images_data_phone_data_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='images',
            new_name='image',
        ),
    ]
