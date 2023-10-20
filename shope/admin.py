from django.contrib import admin
from .models import ContactUs,CheckoutCart, Product, ProductImage, Category, ProductDescription, ParentCategory,Cart, CartItems, Profile


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'in_stock', 'warranty', 'description', 'price', 'image', 'parent', 'discount_percentage', 'arrival']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'is_active']


@admin.register(ProductDescription)
class ProductDescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'description']


@admin.register(ParentCategory)
class ParentCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_paid']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'profile_image']
