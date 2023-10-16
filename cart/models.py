from django.db import models

from product_list.models import ProductList
from users_auth.models import User
from product.models import Product


# Create your models here.

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_list = models.ForeignKey(ProductList, on_delete=models.CASCADE)
