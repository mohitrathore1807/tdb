# Generated by Django 3.0.8 on 2021-04-03 09:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tdbapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leads',
            old_name='city',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='leads',
            old_name='information',
            new_name='help',
        ),
        migrations.AddField(
            model_name='leads',
            name='inquiry_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]