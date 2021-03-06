# Generated by Django 3.0.1 on 2020-01-09 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopUser', '0006_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='product/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopUser.Category')),
            ],
        ),
    ]
