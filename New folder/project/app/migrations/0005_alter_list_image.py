# Generated by Django 5.0.2 on 2024-07-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_list_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
