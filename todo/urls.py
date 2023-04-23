from django.urls import path
from . import views

urlpatterns = [
    path('greetings/', views.greetings),
    path('add/', views.addTodo),
    path('all/', views.getTodos),
    path("update/", views.updateTodo),
    path("delete/", views.deleteTodo)
]
