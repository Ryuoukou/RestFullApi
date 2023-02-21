from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from cars.models import Car

User = get_user_model()

class CarAPITestCase(APITestCase):

    def setUp(self):
        # Создаем пользователя для авторизации в тестах
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Создаем машину для использования в тестах
        self.car = Car.objects.create(vin='12345678901234567', color='green', brand='Honda', car_type=1, user=self.user)

    def test_car_list(self):
        # Проверяем, что запрос списка машин возвращает успешный статус ответа
        url = reverse('car_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_car_detail(self):
        # Проверяем, что запрос детальной информации о машине возвращает успешный статус ответа
        url = reverse('car_detail', args=[self.car.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_car(self):
        # Проверяем, что создание новой машины возвращает успешный статус ответа
        url = reverse('car_create')
        data = {'vin': '12345678901234568', 'color': 'blue', 'brand': 'Toyota', 'car_type': 2}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_car(self):
        # Проверяем, что обновление информации о машине возвращает успешный статус ответа
        url = reverse('car_detail', args=[self.car.id])
        data = {'vin': '12345678901234567', 'color': 'red', 'brand': 'Honda', 'car_type': 1}
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_car(self):
        # Проверяем, что удаление машины возвращает успешный статус ответа
        url = reverse('car_detail', args=[self.car.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



