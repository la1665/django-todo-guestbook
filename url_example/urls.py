from django.urls import path
from . import views


urlpatterns = [
    path('profile/<slug:username>/', views.profile),
    path('profile/', views.profile),

]
