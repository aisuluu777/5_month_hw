# Generated by Django 5.1.6 on 2025-03-11 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_movie_review_review_star_remove_movie_director_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='review',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directors', to='movie_app.director'),
        ),
    ]
