from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.movies_detail_apiview),
    path('', views.movies_list_apiview),
    path('directors/', views.directors_list_create_view),
    path('directors/<int:id>/', views.director_detail_apiview),
    path('reviews/', views.reviews_list_apiview),
    path('reviews/<int:id>/', views.reviews_detail_apiview),
    path('movies/reviews/', views.movies_review_list)]

