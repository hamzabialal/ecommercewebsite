from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.HomeTemplate.as_view(), name= 'home_template'),
    path('faq/', views.FaQsTemplate.as_view(), name='faq_template'),
    path('contactus/', views.ContactTemplate.as_view(), name='contact_template'),
    path('checkoutpayment/', views.CheckOutPayment.as_view(), name='checkoutpayment'),
    path('checkoutinfo/', views.ShippingForm.as_view(), name='checkoutinfo'),
    path('paymentconfirm/', views.PaymentConfirmationView.as_view(), name='paymentconfirm'),
    path('checkoutcart/', views.CheckOutCart.as_view(), name='checkoutcart'),
    path('aboutus/', views.AboutUs.as_view(), name='aboutus'),
    path('myaccount/', views.MyAccount.as_view(), name='myaccount'),
    path('products/<str:category_name>/', views.Products.as_view(), name='products'),
    path('productdetail/', views.ProductDetail.as_view(), name='product_detail'),
    path('searchresults/', views.SearchView.as_view(), name='search_results'),
    path('laptop/', views.Laptop.as_view(), name='laptop'),
    path('desktop/', views.Desktop.as_view(), name='desktop'),
    path('tv/', views.TV.as_view(), name='tv'),
    path('speaker/', views.Speaker.as_view(), name='speaker'),
    path('gadget/', views.Gadget.as_view(), name='gadget'),
    path('register/', views.RegisterForm.as_view(), name='register'),
    path('login/', views.LoginForm.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('addproducts/', views.AddProduct.as_view(), name='addproducts'),
    path('iphonese/', views.IphoneSe.as_view(), name='iphonese'),
    path('applewatch/', views.AppleWatch.as_view(), name='applewatch'),
    path('appleaccessories/', views.AppleAccessories.as_view(), name='appleaccessories'),
    path('macmini', views.MacMini.as_view(), name='macmini'),
    path('macpro/', views.MacPro.as_view(), name='macpro'),
    path('header/', views.Header.as_view(), name='header'),
    path('apple/', views.AppleCategory.as_view(), name='apple_category'),
    path('category/<str:category_name>/', views.CategoryUrl.as_view(), name='category_detail'),
    path('product/<str:product_name>/', views.ProductDetail.as_view(), name='product_detail'),
    path('arrivalproducts/', views.ArrivalProducts.as_view(), name= 'arrivalproducts'),
    path('applewatch/', views.AppleWatch.as_view(), name= 'applewatch'),
    # ... other URL patterns ...
    path('mybackend/', views.get_item_details, name='get_item_details'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('myprofile/', views.UserProfileView.as_view(), name='user_profile'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_cart, name='remove_from_cart'),


                  path('', views.HomeTemplate.as_view(), name='home_template'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
