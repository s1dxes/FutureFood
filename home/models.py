from django.db import models
from users.models import User

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name


class PossibleAllergies(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='food_images')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    allergens = models.ManyToManyField(PossibleAllergies,  blank=True)
    calories = models.PositiveIntegerField(default=0)
    proteins = models.PositiveIntegerField(default=0)
    fats = models.PositiveIntegerField(default=0)
    carbohydrates = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Набор : {self.name} | Категория : {self.category.name}'

class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)
    def total_quantity(self):
        return sum(basket.quantity for basket in self)
    def counter(self):
        return self.count()

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product} '

    def sum(self):
        return self.product.price * self.quantity

