# Generated by Django 3.0.1 on 2020-01-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopUser', '0009_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='myproducts'),
            preserve_default=False,
        ),
    ]
