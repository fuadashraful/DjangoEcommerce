# Generated by Django 3.0.1 on 2020-01-09 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopUser', '0013_auto_20200109_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]