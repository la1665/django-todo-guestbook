from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo-index'),
    path('add/', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete/', views.deleteCompleted, name='delete-complete'),
    path('deletecompleteall/', views.deleteAll, name='delete-all'),
    
    
]