# Generated by Django 5.0.2 on 2024-07-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_data_age_remove_data_img_remove_data_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='images',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='phone',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='place',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
