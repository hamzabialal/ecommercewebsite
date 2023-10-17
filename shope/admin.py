from django.contrib import admin
from .models import ContactUs,CheckoutCart, Product, ProductImage, Category, ProductDescription, ParentCategory,CreateCard,StripePaymentIntentId


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
admin.site.register(StripePaymentIntentId)
admin.site.register(CreateCard)
admin.site.register(CheckoutCart)

