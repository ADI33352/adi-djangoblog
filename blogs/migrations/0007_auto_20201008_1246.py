# Generated by Django 3.1.1 on 2020-10-08 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20201008_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='', upload_to='blogs'),
        ),
    ]
