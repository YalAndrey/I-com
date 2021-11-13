from django.db import models


class Video_games(models.Model):
    title = models.TextField(max_length='60')
    description = models.TextField()
    mark = models.IntegerField()
    cover = models.ImageField(upload_to=('img/video_games/'))
    Screen_shot_one = models.ImageField(upload_to='img/video_games/')
    Screen_shot_two = models.ImageField(upload_to='img/video_games/')
    Screen_shot_three = models.ImageField(upload_to='img/video_games/')
    metacritic_url = models.TextField()
    trailer = models.TextField()
    My_ot = models.TextField()
    Data_exit = models.DateTimeField()
    Isdatel = models.TextField()
    awards = models.TextField()
    where_start = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео игра'
        verbose_name_plural = 'Видео игры'


