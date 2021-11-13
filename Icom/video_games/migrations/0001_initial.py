# Generated by Django 3.2.7 on 2021-11-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video_games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length='60')),
                ('description', models.TextField()),
                ('mark', models.IntegerField()),
                ('cover', models.ImageField(upload_to='img/video_games/')),
                ('Screen_shot_one', models.ImageField(upload_to='img/video_games/')),
                ('Screen_shot_two', models.ImageField(upload_to='img/video_games/')),
                ('Screen_shot_tree', models.ImageField(upload_to='img/video_games/')),
                ('metacritic_url', models.TextField()),
                ('trailer', models.TextField()),
                ('My_ot', models.TextField()),
                ('Data_exit', models.DateTimeField()),
                ('Isdatel', models.TextField()),
                ('awards', models.TextField()),
                ('where_start', models.TextField()),
            ],
            options={
                'verbose_name': 'Видео игра',
                'verbose_name_plural': 'Видео игры',
            },
        ),
    ]