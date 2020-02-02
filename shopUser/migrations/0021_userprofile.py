# Generated by Django 3.0.1 on 2020-01-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopUser', '0020_product_uploaded_from'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('userImage', models.ImageField(upload_to='profile_image')),
            ],
        ),
    ]