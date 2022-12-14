from category.models import Category
from django.db import models
from django.core.validators import MinValueValidator 

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500,blank=True)
    price = models.FloatField(validators=[MinValueValidator(1)])
    images = models.ImageField(upload_to='photos/products')
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name