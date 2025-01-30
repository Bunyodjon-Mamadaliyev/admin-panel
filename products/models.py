from django.db import models
from django.shortcuts import reverse
from categories.base_models import BaseModel
from categories.models import Category


class Product(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def get_detail_url(self):
        return reverse('products:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('products:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('products:delete', args=[self.pk])

    def __str__(self):
        return self.name
