# Generated by Django 3.2 on 2021-04-18 10:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tdbapp', '0005_auto_20210418_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uid',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
