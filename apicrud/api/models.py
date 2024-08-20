from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,related_name="subcategories",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField(default=0, blank=True)
    sale_price = models.FloatField(default=0, blank=True)
    stock = models.IntegerField(default=0, blank=True)
    codigo = models.CharField(max_length=12)
    color = models.ForeignKey(Color, related_name="products",on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory,related_name="products",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name