from django.contrib import admin
from .models import ContactUs, Product, ProductImage


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'availability', 'warranty', 'display_description', 'price', 'original_price', 'product_description','first_image', 'parent']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display  = ['id', 'image']