from django.urls import path
from . import views
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
]
