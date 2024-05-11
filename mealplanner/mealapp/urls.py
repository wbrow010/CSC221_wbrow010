"""Defines URL patterns for mealapp."""

from django.urls import path

from . import views

app_name = 'mealapp'

urlpatterns = [

    path('', views.index, name='index'),
    path('remove-all-meals/', views.remove_all_meals, name='remove_all_meals'), 
    path('meals/', views.meals, name='meals'),
    path('meal/<int:meal_id>/', views.meal, name='meal'),
]