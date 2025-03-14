from django.contrib import admin
from django.urls import path, include
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.directors_list_create_view),
    path('api/v1/directors/<int:id>/', views.director_detail_apiview),
    path('api/v1/movies/', views.movies_list_apiview),
    path('api/v1/movies/<int:id>/', views.movies_detail_apiview),
    path('api/v1/reviews/', views.reviews_list_apiview),
    path('api/v1/reviews/<int:id>/', views.reviews_detail_apiview),
    path('api/v1/movies/reviews/', views.movies_review_list)
]

