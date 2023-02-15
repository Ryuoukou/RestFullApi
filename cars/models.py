from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Car(models.Model):
    #Модель базы данных в которой есть все необходимое для идентефикации машины
    vin = models.CharField(verbose_name='Вин', db_index=True, unique=True, max_length=200)
    color = models.CharField(verbose_name='Цвет', max_length=200)
    brand = models.CharField(verbose_name='Бренд', max_length=200)
    CAR_TYPES = (
        #В данном случае создаю список из 4 типом машин которые буду использовать в car_type а именно в аргумент choices
        (1, 'Седан'),
        (2, 'Хэчбек'),
        (3, 'Универсал'),
        (4, 'Купе'),
    )
    car_type = models.IntegerField(verbose_name='Тип машины', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE) #Параметр User будет работать только после импорта get_user_model(класс модели который используется для представления пользователя)
