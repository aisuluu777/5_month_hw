# Generated by Django 5.1.6 on 2025-03-11 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_movie_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='review',
        ),
    ]
