import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.db.models import Count
from .manager import *


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
    slug = models.SlugField(unique=True, null=True, blank=True)

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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # Use self.title, not self.product_name
        super(Product, self).save(*args, **kwargs)

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


class CheckoutCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    total = models.IntegerField(default=0, null=True, blank=True)


class StripePaymentIntentId(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    payment_intent_id = models.CharField(max_length=255, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)


class ShippingAddress(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    comp_name = models.CharField(max_length=255, null=True, blank=True)
    area_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=255, default='')
    zip_code = models.CharField(max_length=20)
    busines_address = models.BooleanField(default=False, null=True, blank=True)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default = False)

    def __str__(self):
        return self.user.username


class CreateCard(models.Model):
    name = models.CharField(max_length=30)
    card_number = models.IntegerField()
    exp_year = models.CharField(max_length=30)
    exp_month = models.CharField(max_length=30)
    CSV = models.IntegerField()


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1, null=False, blank=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_image = models.ImageField(upload_to='profile')



    def get_cart_count(self):
        return self.user.cart_set.filter(is_paid=False).aggregate(cart_count=Count('cart_items'))['cart_count']

#
# class CustomUser(AbstractUser):
#     username = None
#     emails = models.EmailField(unique=True)
#     phone_no = models.CharField(max_length=15, default='')
#     is_phone_verified = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#
