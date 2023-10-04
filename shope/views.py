from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ContactForm, SignUpForm, LoginForm, ProductForm
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class HomeTemplate(TemplateView):
    template_name = 'index.html'
class FaQsTemplate(TemplateView):
    template_name = 'faq.html'
class ContactTemplate(FormView):
    template_name = 'contact_us.html'
    form_class = ContactForm
    success_url = '/products/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

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
class Tablets(TemplateView):
    template_name = 'tablets.html'
class Laptop(TemplateView):
    template_name = 'laptop.html'
class Desktop(TemplateView):
    template_name= 'desktop.html'
class TV(TemplateView):
    template_name = 'tv.html'
class Speaker(TemplateView):
    template_name = 'speaker.html'
class Gadget(TemplateView):
    template_name = 'gadget.html'
class RegisterForm(FormView):
    template_name= 'register.html'
    form_class = SignUpForm
    success_url = '/products/'
    def form_valid(self, form):
        user = form.save()
        messages.add_message(self.request, messages.SUCCESS, "Congrats")
        return super().form_valid(form)
class LoginForm(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/contactus/'

    def form_valid(self, form):
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, "Successfully Logged In!")
            return super().form_valid(form)
        return self.form_invalid(form)
class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
class AddProduct(FormView):
    template_name = 'addproduct.html'
    form_class = ProductForm
    success_url = '/products/'

    def form_valid(self, form):
            form.save()
            return super().form_valid(form)
