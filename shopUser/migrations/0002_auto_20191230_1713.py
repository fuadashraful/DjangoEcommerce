# Generated by Django 3.0.1 on 2019-12-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentoffer',
            name='offerName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='currentoffer',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
