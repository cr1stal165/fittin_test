from django.db import models
import uuid as uuid

from product_list.models import ProductList
from users_auth.models import User


# Create your models here.


class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    order_date = models.DateField()
    date_of_receiving = models.DateField()
    address = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Заказ {self.order_number}'
