from wsgiref.validate import validator

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers
from .models import Director, Movie, Review
from . import serializers
from django.db import transaction


@api_view(['GET', 'POST'])
def directors_list_create_view(request):
    if request.method == 'GET':
        directors = models.Director.objects.all()
        serializer =  serializers.DirectorSerializer( instance=directors, many=True)
        return Response(data=serializer.data,status=200)
    elif request.method == 'POST':
        validator = serializers.DirectorValidateSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        name = request.data.get('name')
        director = models.Director.objects.create(name=name)
        return Response(data=serializers.DirectorValidateSerializer(director).data, status=201)


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
        validator = serializers.DirectorValidateSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        director.name = request.data.get('name')
        director.save()
        return Response(data=serializers.DirectorValidateSerializer(director).data
                        ,status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def movies_list_apiview(request):
    if request.method == 'GET':
        movies = models.Movie.objects.select_related('director')
        serializer = serializers.MovieSerializer( instance=movies, many=True)
        return Response(data=serializer.data,status=200)
    elif request.method == 'POST':
        validator = serializers.MovieValidateSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = models.Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id)
        return Response(data=serializers.MovieValidateSerializer(movie).data, status=201)


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
        validator = serializers.MovieValidateSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        with transaction.atomic():
            movie.title = request.data.get('title')
            movie.description = request.data.get('description')
            movie.duration = request.data.get('duration')
            movie.director_id = request.data.get('director_id')
            movie.save()
            return Response(data=serializers.MovieValidateSerializer(movie).data, status=201)

@api_view(['GET', 'POST'])
def reviews_list_apiview(request):
    if request.method == 'GET':
        reviews = models.Review.objects.select_related('movie')
        serializer = serializers.ReviewSerializer( instance=reviews, many=True)
        return Response(data=serializer.data,status=200)
    elif request.method == 'POST':
        validator = serializers.ReviewValidateSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        star = request.data.get('star')
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        movie = models.Review.objects.create(
            star=star,
            text=text,
            movie_id=movie_id
        )
        return Response(data=serializers.ReviewValidateSerializer(movie).data, status=201)

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
        validator = serializers.ReviewValidateSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        review.star = request.data.get('star')
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.save()
        return Response(data=serializers.ReviewValidateSerializer(review).data, status=201)


@api_view(['GET'])
def movies_review_list(request):
    review_lst = models.Movie.objects.select_related('director').prefetch_related('reviews')
    serializer = serializers.MovieReviewSerializer(review_lst, many=True)
    return Response(data=serializer.data,status=200)

