# Generated by Django 3.0.6 on 2020-06-10 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='sample.jpg', upload_to='profile_pics'),
        ),
    ]
