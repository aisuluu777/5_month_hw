from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name', 'movies_count']

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'



class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields =['title', 'description', 'duration','reviews_detail', 'average_rating']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration']


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200, required=True)
    description = serializers.CharField(max_length=500, required=True)
    duration = serializers.CharField(max_length=200, required=True)
    director_id = serializers.IntegerField(required=True)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise serializers.ValidationError("Director does not exist")
        return director_id

    # def validate_title(self, title):
    #     if Movie.objects.filter(title=title).exists():
    #         raise serializers.ValidationError("Film with this title is already exists, please choose another title")
    #     return title

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewValidateSerializer(serializers.Serializer):
    star = serializers.IntegerField(required=True, min_value=1, max_value=5)
    text = serializers.CharField(required=True)
    movie_id = serializers.IntegerField(required=True)

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

