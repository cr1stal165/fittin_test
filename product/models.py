import uuid as uuid
from django.db import models

from category.models import Category


# Create your models here.


class Product(models.Model):
    article_uuid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    description = models.CharField()
    price = models.IntegerField()
    supplier = models.CharField()
    image = models.ImageField(null=True, upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
