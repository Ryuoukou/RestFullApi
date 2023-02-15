from django.contrib import admin
from django.urls import path, include
from cars.views import *

app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view()), #url переводящий на страницу для создания и добавления машины в бд
    path('all/', CarsListView.as_view()), #url переводящий на страницу для просмотра всех созданных машин т.е CarsListView в cars\views.py
    path('car/detail/<int:pk>/', CarDetailView.as_view()),

]
