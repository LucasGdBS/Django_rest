from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.get_users, name='get_users'),
    path('users/<str:pk>/', views.get_user, name='get_user'),
    path('data/', views.user_manager, name='user_manager'),
]