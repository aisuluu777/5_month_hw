from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers
from .models import Director, Movie, Review


@api_view(['GET'])
def directors_list_apiview(request):
    directors = models.Director.objects.all()
    serializer =  serializers.DirectorSerializer( instance=directors, many=True)
    return Response(data=serializer.data,status=200)

@api_view(['GET'])
def director_detail_apiview(request, id):
    try:
        director = models.Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error':'Page Not Found'},status=404)
    data = serializers.DirectorDetailSerializer(director, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movies_list_apiview(request):
    movies = models.Movie.objects.all()
    serializer = serializers.MovieSerializer( instance=movies, many=True)
    return Response(data=serializer.data,status=200)

@api_view(['GET'])
def movies_detail_apiview(request, id):
    try:
        movie = models.Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error':'Page Not Found'},status=404)
    data = serializers.MovieDetailSerializer(movie, many=False).data
    return Response(data=data)

@api_view(['GET'])
def reviews_list_apiview(request):
    reviews = models.Review.objects.all()
    serializer = serializers.ReviewSerializer( instance=reviews, many=True)
    return Response(data=serializer.data,status=200)

@api_view(['GET'])
def reviews_detail_apiview(request, id):
    try:
        review = models.Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error':'Page Not Found'},status=404)
    data = serializers.ReviewDetailSerializer(review, many=False).data
    return Response(data=data)

@api_view(['GET'])
def movies_review_list(request):
    review_lst = models.Movie.objects.all()
    serializer = serializers.MovieSerializer(review_lst, many=True)
    return Response(data=serializer.data,status=200)
