from django.db import models


class Comics(models.Model):
    image_one = models.ImageField(upload_to='img/')
    image_two = models.ImageField(upload_to='img/')
    title = models.TextField(max_length=20)
    mark = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комикс'
        verbose_name_plural = 'Комиксы'
