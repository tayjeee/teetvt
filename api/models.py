from datetime import timezone
from django.db import models

# Create your models here.


class Store(models.Model):
    store_id = models.IntegerField(unique=True)
    store_location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.store_id} - {self.store_location} - {self.created_at} - {self.updated_at}"

class Product(models.Model):
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=100)
    created_att = models.DateTimeField(auto_now_add=True)
    updated_att = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_id} - {self.product_name} - {self.created_att} - {self.updated_att}"