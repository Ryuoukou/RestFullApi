from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarListSerializer
from cars.permissions import IsOwnerOrReadOnly
from cars.models import Car
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class CarCreateView(generics.CreateAPIView):
    #View для создания машины
    serializer_class = CarDetailSerializer

class CarsListView(generics.ListAPIView):
    #View для просмотра всех созданных машин
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser, )

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    #View для просмотра, редактирования и удаления отдельной записи
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )