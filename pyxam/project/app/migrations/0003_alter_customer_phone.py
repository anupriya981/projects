# Generated by Django 5.0.6 on 2024-07-13 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customer_img_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.TextField(max_length=10),
        ),
    ]
