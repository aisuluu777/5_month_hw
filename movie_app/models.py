from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


    def movies_count(self):
        return self.directors.count()


class Review(models.Model):
    STARS = (
        (star, '* ' * star) for star in range(1, 6)
    )
    star = models.IntegerField(choices=STARS, default=4)
    text = models.TextField()
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.text


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Введит название фильма')
    description = models.TextField(verbose_name='Введите краткое описание фильма')
    duration = models.CharField(max_length=50 ,verbose_name='Укажите длительеость фильма')
    director = models.ForeignKey(Director, blank=True, null=True, on_delete=models.CASCADE, related_name='directors')


    def __str__(self):
        return self.title

    def reviews_detail(self):
        return [review.text for review in self.movies.all()]


    def average_rating(self):
        reviews = self.movies.all()
        total_stars = sum(review.star for review in reviews)
        count = reviews.count()

        if count == 0:
            return "Рейтинг отсутствует"

        return round(total_stars / count, 2)



