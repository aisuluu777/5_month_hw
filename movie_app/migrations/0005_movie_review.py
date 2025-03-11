# Generated by Django 5.1.6 on 2025-03-11 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_remove_movie_review_remove_movie_director_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie_app.review'),
        ),
    ]
