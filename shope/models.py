import uuid

from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    subject = models.TextField(max_length=200)
    message = models.TextField(max_length=1000)


class ParentCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    parent_category = models.ForeignKey(ParentCategory, on_delete=models.CASCADE, related_name='parent_category', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    in_stock = models.BooleanField(default=True)
    warranty = models.PositiveIntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='shop/images', default="")
    is_active = models.BooleanField(default=True)
    parent = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products", null=True, blank=True)
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=0,default=0)
    is_featured = models.BooleanField(default=True)
    arrival = models.BooleanField(default='')

    def __str__(self):
        return self.title

    @property
    def discounted_price(self):
        discount_amount = (self.discount_percentage / 100) * self.price
        discounted_price = self.price - discount_amount
        return discounted_price


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(upload_to='shop/images', default="")


class ProductDescription(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_description", null=True, blank=True)
    title = models.CharField(max_length=130, default="")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='shop/images', default="")


class ShippingAddress(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    company_name = models.CharField(max_length=67, blank=True)
    area_code = models.CharField(max_length=5)
    primary_field = models.CharField(max_length=20)
    street_address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=13)
    business_address = models.BooleanField()


class CardInformation(models.Model):
    cardholder_name = models.CharField(max_length=200)
    card_number = models.CharField(max_length=16)
    payment_types = models.CharField(max_length=200)
    expiration_data = models.CharField(max_length=200)
    csc = models.CharField(max_length=3)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_keys=True)
    order_id = models.IntegerField(default= '')



