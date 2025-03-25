from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.RegisterApiView.as_view()),
    path('confirm/', views.ConfirmApiView.as_view()),
    path('authorization/', views.AuthorizationApiView.as_view()),
]