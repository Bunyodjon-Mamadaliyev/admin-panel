from django.db import models
from django.utils.text import slugify
from .base_models import BaseModel
from django.shortcuts import reverse


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='category_icons/', blank=True, null=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('categories:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def get_update_url(self):
        return reverse('categories:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('categories:delete', args=[self.pk])

    class Meta:
        verbose_name_plural = "Categories"
