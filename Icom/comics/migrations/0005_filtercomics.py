# Generated by Django 3.2.7 on 2021-11-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0004_alter_comics_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterComics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marvel', models.BooleanField()),
                ('dc', models.BooleanField()),
                ('dark_horse', models.BooleanField()),
                ('bubble', models.BooleanField()),
                ('other', models.BooleanField()),
                ('mark', models.TextField()),
            ],
            options={
                'verbose_name': 'КомиксФильтр',
                'verbose_name_plural': 'КомиксыФильтр',
            },
        ),
    ]
