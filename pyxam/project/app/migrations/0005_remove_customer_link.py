# Generated by Django 5.0.6 on 2024-07-13 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_customer_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='link',
        ),
    ]
