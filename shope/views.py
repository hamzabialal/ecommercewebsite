from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomeTemplate(TemplateView):
    template_name = 'index.html'
class FaQsTemplate(TemplateView):
    template_name = 'faq.html'
class ContactTemplate(TemplateView):
    template_name = 'contact_us.html'

class CheckOutPayment(TemplateView):
    template_name = 'checkout_payment.html'
class CheckOutInfo(TemplateView):
    template_name = 'checkout_info.html'
class CheckOutComplete(TemplateView):
    template_name= 'checkout_complete.html'
class CheckOutCart(TemplateView):
    template_name= 'checkout_cart.html'
class AboutUs(TemplateView):
    template_name= 'about_us.html'
class MyAccount(TemplateView):
    template_name= 'my_account.html'
class Products(TemplateView):
    template_name = 'product.html'
class ProductDetail(TemplateView):
    template_name = 'product_detail.html'
class SearchResults(TemplateView):
    template_name = 'search_results.html'
class MobilePhones(TemplateView):
    template_name = 'mobile_phone.html'
