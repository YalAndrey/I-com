# Generated by Django 3.2.7 on 2021-11-11 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0006_auto_20211111_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comics',
            name='isdatel',
            field=models.TextField(default='other', max_length=60),
        ),
    ]
