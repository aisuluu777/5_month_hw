from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register_api_view),
    path('activate/', views.activate_user_api_view),
    path('authorization/', views.authorization_api_view)

]