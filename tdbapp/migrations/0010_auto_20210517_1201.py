# Generated by Django 3.1.8 on 2021-05-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tdbapp', '0009_auto_20210517_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='post',
            name='keywords',
            field=models.TextField(default=None),
        ),
    ]