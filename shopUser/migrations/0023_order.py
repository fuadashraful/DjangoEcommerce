# Generated by Django 3.0.1 on 2020-02-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopUser', '0022_auto_20200130_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_by', models.IntegerField(default=0)),
                ('product_id', models.IntegerField(default=0)),
                ('payment_method', models.CharField(choices=[('B', 'Bkash'), ('R', 'Rocket'), ('N', 'Nogod'), ('U', 'Upay')], max_length=1)),
            ],
        ),
    ]