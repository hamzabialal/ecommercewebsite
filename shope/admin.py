from django.contrib import admin
from .models import ContactUs,OrderTracker,AddititonalInformation, Reviews, ShippingAddress, Product, ProductImage, Category, ProductDescription, ParentCategory,Cart, CartItems, Profile


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'in_stock', 'warranty', 'description', 'price', 'image', 'parent', 'discount_percentage', 'arrival','slug']


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


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'comp_name', 'area_code', 'phone', 'address', 'zip_code', 'busines_address']


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'review', 'rating', 'created_at']


@admin.register(AddititonalInformation)
class AddititonalInformationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'main_title', 'main_title1','description1', 'description2']


@admin.register(OrderTracker)
class OrderTrackerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'delivered','tracking_id']

