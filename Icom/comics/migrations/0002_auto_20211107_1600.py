# Generated by Django 3.2.7 on 2021-11-07 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comics',
            name='image_one',
            field=models.ImageField(upload_to='static/img'),
        ),
        migrations.AlterField(
            model_name='comics',
            name='image_two',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]