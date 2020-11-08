# Generated by Django 3.1.1 on 2020-10-11 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_auto_20201009_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('thumbnail', models.ImageField(default='', upload_to='thumbnails')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='blogs.Category')),
            ],
        ),
    ]
