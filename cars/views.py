from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarListSerializer
from cars.permissions import IsOwnerOrReadOnly
from cars.models import Car
from rest_framework.permissions import IsAdminUser, AllowAny


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
    permission_classes = (AllowAny, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (AllowAny, )


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )