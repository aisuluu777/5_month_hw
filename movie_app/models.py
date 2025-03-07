from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Введит название фильма')
    description = models.TextField(verbose_name='Введите краткое описание фильма')
    duration = models.CharField(max_length=50 ,verbose_name='Укажите длительеость фильма')
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

