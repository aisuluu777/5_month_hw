from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from .models import Director, Movie, Review
from . import serializers
from django.db import transaction
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

class DirectorList(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = serializers.DirectorSerializer

    def create(self, request, *args, **kwargs):
        validator = serializers.DirectorValidateSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        name = validator.validated_data.get('name')
        director = Director.objects.create(name=name)
        return Response(data=serializers.DirectorValidateSerializer(director).data, status=201)


class DirectorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = serializers.DirectorSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        director = Director.objects.get(id=kwargs['id'])
        validator = serializers.DirectorValidateSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        director.name = validator.validated_data.get('name')
        director.save()
        return Response(data=serializers.DirectorValidateSerializer(director).data
                        , status=status.HTTP_201_CREATED)


class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    pagination_class = PageNumberPagination


    def create(self, request, *args, **kwargs):
        validator = serializers.MovieValidateSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        title = validator.validated_data.get('title')
        description = validator.validated_data.get('description')
        duration = validator.validated_data.get('duration')
        director_id = validator.validated_data.get('director_id')
        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id)
        return Response(data=serializers.MovieValidateSerializer(movie).data, status=201)


class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        movie = Movie.objects.get(id=kwargs['id'])
        validator = serializers.MovieValidateSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        movie.title = validator.validated_data.get('title')
        movie.description = validator.validated_data.get('description')
        movie.duration = validator.validated_data.get('duration')
        movie.director_id = validator.validated_data.get('director_id')
        movie.save()
        return Response(data=serializers.MovieValidateSerializer(movie).data, status=201)


class ReviewList(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer


    def create(self, request, *args, **kwargs):
        validator = serializers.ReviewValidateSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        star = validator.validated_data.get('star')
        text = validator.validated_data.get('text')
        movie_id = validator.validated_data.get('movie_id')
        movie = models.Review.objects.create(
            star=star,
            text=text,
            movie_id=movie_id
        )
        return Response(data=serializers.ReviewValidateSerializer(movie).data, status=201)


class ReviewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        review = Review.objects.get(id=kwargs['id'])
        validator = serializers.ReviewValidateSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        review.star = validator.validated_data.get('star')
        review.text = validator.validated_data.get('text')
        review.movie_id = validator.validated_data.get('movie_id')
        review.save()
        return Response(data=serializers.ReviewValidateSerializer(review).data, status=201)


class MoviesReviewListView(ListAPIView ):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieReviewSerializer









    # @api_view(['GET', 'POST'])
    # def directors_list_create_view(request):
    #     if request.method == 'GET':
    #         directors = models.Director.objects.all()
    #         serializer =  serializers.DirectorSerializer( instance=directors, many=True)
    #         return Response(data=serializer.data,status=200)
    #     elif request.method == 'POST':
    #         validator = serializers.DirectorValidateSerializer(data=request.data)
    #         validator.is_valid(raise_exception=True)
    #         name = validator.validated_data.get('name')
    #         director = models.Director.objects.create(name=name)
    #         return Response(data=serializers.DirectorValidateSerializer(director).data, status=201)



    # @api_view(['GET', 'PUT', 'DELETE'])
    # def director_detail_apiview(request, id):
    #     try:
    #         director = models.Director.objects.get(id=id)
    #     except Director.DoesNotExist:
    #         return Response(data={'error':'Page Not Found'},status=404)
    #     if request.method == 'GET':
    #         data = serializers.DirectorDetailSerializer(director, many=False).data
    #         return Response(data=data)
    #     elif request.method == 'DELETE':
    #         director.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     elif request.method == 'PUT':
    #         validator = serializers.DirectorValidateSerializer(data=request.data)
    #         validator.is_valid(raise_exception=True)
    #         director.name = validator.validated_data.get('name')
    #         director.save()
    #         return Response(data=serializers.DirectorValidateSerializer(director).data
    #                         ,status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def movies_list_apiview(request):
#     if request.method == 'GET':
#         movies = models.Movie.objects.select_related('director')
#         serializer = serializers.MovieSerializer( instance=movies, many=True)
#         return Response(data=serializer.data,status=200)
#     elif request.method == 'POST':
#         validator = serializers.MovieValidateSerializer(data=request.data)
#         validator.is_valid(raise_exception=True)
#         title = validator.validated_data.get('title')
#         description = validator.validated_data.get('description')
#         duration = validator.validated_data.get('duration')
#         director_id = validator.validated_data.get('director_id')
#         movie = models.Movie.objects.create(
#             title=title,
#             description=description,
#             duration=duration,
#             director_id=director_id)
#         return Response(data=serializers.MovieValidateSerializer(movie).data, status=201)

# @api_view(['GET', 'POST'])
# def movies_list_apiview(request):
#     if request.method == 'GET':
#         movies = models.Movie.objects.select_related('director')
#         serializer = serializers.MovieSerializer( instance=movies, many=True)
#         return Response(data=serializer.data,status=200)
#     elif request.method == 'POST':
#         validator = serializers.MovieValidateSerializer(data=request.data)
#         validator.is_valid(raise_exception=True)
#         title = validator.validated_data.get('title')
#         description = validator.validated_data.get('description')
#         duration = validator.validated_data.get('duration')
#         director_id = validator.validated_data.get('director_id')
#         movie = models.Movie.objects.create(
#             title=title,
#             description=description,
#             duration=duration,
#             director_id=director_id)
#         return Response(data=serializers.MovieValidateSerializer(movie).data, status=201)


# @api_view(['GET', 'POST'])
# def reviews_list_apiview(request):
#     if request.method == 'GET':
#         reviews = models.Review.objects.select_related('movie')
#         serializer = serializers.ReviewSerializer( instance=reviews, many=True)
#         return Response(data=serializer.data,status=200)
#     elif request.method == 'POST':
#         validator = serializers.ReviewValidateSerializer(data=request.data)
#         validator.is_valid(raise_exception=True)
#         star = validator.validated_data.get('star')
#         text = validator.validated_data.get('text')
#         movie_id = validator.validated_data.get('movie_id')
#         movie = models.Review.objects.create(
#             star=star,
#             text=text,
#             movie_id=movie_id
#         )
#         return Response(data=serializers.ReviewValidateSerializer(movie).data, status=201)

# @api_view(['GET', 'PUT', 'DELETE'])
# def reviews_detail_apiview(request, id):
#     try:
#         review = models.Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'error':'Page Not Found'},status=404)
#     if request.method == 'GET':
#         data = serializers.ReviewDetailSerializer(review, many=False).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         validator = serializers.ReviewValidateSerializer(data=request.data)
#         validator.is_valid(raise_exception=True)
#         review.star = validator.validated_data.get('star')
#         review.text = validator.validated_data.get('text')
#         review.movie_id = validator.validated_data.get('movie_id')
#         review.save()
#         return Response(data=serializers.ReviewValidateSerializer(review).data, status=201)
#







