from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers
from .models import Director, Movie, Review
from .serializers import DirectorDetailSerializer, MovieDetailSerializer, ReviewDetailSerializer
from django.db import transaction


@api_view(['GET', 'POST'])
def directors_list_create_view(request):
    if request.method == 'GET':
        directors = models.Director.objects.all()
        serializer =  serializers.DirectorSerializer( instance=directors, many=True)
        return Response(data=serializer.data,status=200)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = models.Director.objects.create(name=name)
        return Response(data=DirectorDetailSerializer(director).data, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_apiview(request, id):
    try:
        director = models.Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error':'Page Not Found'},status=404)
    if request.method == 'GET':
        data = serializers.DirectorDetailSerializer(director, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorDetailSerializer(director).data
                        ,status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def movies_list_apiview(request):
    if request.method == 'GET':
        movies = models.Movie.objects.select_related('director')
        serializer = serializers.MovieSerializer( instance=movies, many=True)
        return Response(data=serializer.data,status=200)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = models.Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id)
        return Response(MovieDetailSerializer(movie).data, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail_apiview(request, id):
    try:
        movie = models.Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error':'Page Not Found'},status=404)
    if request.method == 'GET':
        data = serializers.MovieDetailSerializer(movie, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data=MovieDetailSerializer(movie).data, status=201)

@api_view(['GET', 'POST'])
def reviews_list_apiview(request):
    if request.method == 'GET':
        reviews = models.Review.objects.select_related('movie')
        serializer = serializers.ReviewSerializer( instance=reviews, many=True)
        return Response(data=serializer.data,status=200)
    elif request.method == 'POST':
        star = request.data.get('star')
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        movie = models.Review.objects.create(
            star=star,
            text=text,
            movie_id=movie_id
        )
        return Response(ReviewDetailSerializer(movie).data, status=201)

@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_apiview(request, id):
    try:
        review = models.Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error':'Page Not Found'},status=404)
    if request.method == 'GET':
        data = serializers.ReviewDetailSerializer(review, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        review.star = request.data.get('star')
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.save()
        return Response(ReviewDetailSerializer(review).data, status=201)


@api_view(['GET'])
def movies_review_list(request):
    review_lst = models.Movie.objects.all()
    serializer = serializers.MovieReviewSerializer(review_lst, many=True)
    return Response(data=serializer.data,status=200)

