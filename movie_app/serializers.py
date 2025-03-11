from rest_framework import serializers
from . import models

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = ['name', 'movies_count']

class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ['title', 'description', 'duration','reviews_detail', 'average_rating']



class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'