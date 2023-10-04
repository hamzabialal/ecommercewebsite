from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.HomeTemplate.as_view(), name= 'home_template'),
    path('faq/', views.FaQsTemplate.as_view(), name = 'faq_template'),
    path('contactus/', views.ContactTemplate.as_view(), name= 'contact_template'),
    path('checkoutpayment/',views.CheckOutPayment.as_view(), name= 'checkoutpayment'),
    path('checkoutinfo/', views.CheckOutInfo.as_view(), name= 'checkoutinfo'),
    path('checkoutcomplete/', views.CheckOutComplete.as_view(), name= 'checkoutcomplete'),
    path('checkoutcart/', views.CheckOutCart.as_view(), name= 'checkoutcart'),
    path('aboutus/', views.AboutUs.as_view(), name= 'aboutus'),
    path('myaccount/', views.MyAccount.as_view(), name= 'myaccount'),
    path('products/', views.Products.as_view(), name= 'products'),
    path('productdetail/', views.ProductDetail.as_view(), name= 'product_detail'),
    path('searchresults/', views.SearchResults.as_view(), name= 'search_results'),
    path('mobilephone/', views.MobilePhones.as_view(), name= 'mobilephone'),
    path('tablets/', views.Tablets.as_view(), name='tablets'),
    path('laptop/', views.Laptop.as_view(), name= 'laptop'),
    path('desktop/', views.Desktop.as_view(), name= 'desktop'),
    path('tv/', views.TV.as_view(), name= 'tv'),
    path('speaker/', views.Speaker.as_view(), name= 'speaker'),
    path('gadget/', views.Gadget.as_view(), name= 'gadget'),
    path('register/', views.RegisterForm.as_view(), name= 'register'),
    path('login/', views.LoginForm.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name= 'logout'),
    path('addproducts/', views.AddProduct.as_view(), name= 'addproducts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
