# Generated by Django 3.0.1 on 2020-02-01 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopUser', '0025_order_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
