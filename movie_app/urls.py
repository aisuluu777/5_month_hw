from django.urls import path
from . import views


urlpatterns = [
    path('', views.MovieList.as_view()),
    path('<int:id>/', views.MovieDetail.as_view()),
    path('directors/', views.DirectorList.as_view()),
    path('directors/<int:id>/', views.DirectorDetail.as_view()),
    path('reviews/', views.ReviewList.as_view()),
    path('reviews/<int:id>/', views.ReviewDetail.as_view()),
    path('movies/reviews/', views.MoviesReviewListView.as_view()),
]

