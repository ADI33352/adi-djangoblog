# Generated by Django 3.1.1 on 2020-10-09 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_auto_20201008_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='image',
            new_name='imagee',
        ),
    ]
