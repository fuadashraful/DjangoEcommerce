# Generated by Django 3.0.1 on 2020-02-02 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopUser', '0026_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transection_no',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
    ]
