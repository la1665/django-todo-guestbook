from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='user_index'),
    path('register/', views.register, name='register'),
]
