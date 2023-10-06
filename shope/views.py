from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from .forms import ContactForm, SignUpForm, LoginForm, ProductForm
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import Product, Category

# Create your views here.
class HomeTemplate(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        # You can define a queryset here or return an empty queryset
        return Product.objects.all()  # For example, fetching products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch data from the Category model
        context['categories'] = Category.objects.all()

        # Fetch data from the Product model
        context['products'] = self.get_queryset()

        return context



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
# class MobilePhones(ListView):
#     template_name = 'mobile_phone.html'
#     model = Product
#     context_object_name= 'mobile_phones'
#     def get_queryset(self):
#         return self.model.objects.filter(Major_category = 'Phones')
# class Tablets(ListView):
#     template_name = 'tablets.html'
#     model = Product
#     context_object_name = 'tablets'
#     def get_queryset(self):
#         return self.model.objects.filter(Major_category = 'Tablets')
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
class IphoneSe(ListView):
    template_name = 'iphonese.html'
    model = Product
    context_object_name = 'iphone_listings'

    def get_queryset(self):
        # Define the 'parent' parameter you want to filter by
        parent_param = 'Apple> I Phone'  # Note the spaces around the '>' symbol

        # Debugging: Print the 'parent_param' to check if it's correctly set
        print("Parent Parameter:", parent_param)

        # Filter products based on the selected 'parent' parameter
        queryset = self.model.objects.filter(parent__category=parent_param)

        # Debugging: Print the resulting queryset to check its contents
        print("Filtered QuerySet:", queryset)

        return queryset

class IphoneSecategry(ListView):
    template_name = 'iphonese.html'

    model = Product
    context_object_name = 'categories'

    def get_queryset(self):
        category = self.kwargs.get('parent')
        if category:
            return self.model.objects.filter(parent=category)
        else:
            return self.model.objects.all()
class AppleWatch(TemplateView):
    template_name = 'applewatch.html'
class AppleAccessories(TemplateView):
    template_name = 'appleaccessories.html'
class MacMini(TemplateView):
    template_name = 'macmini.html'
class MacPro(TemplateView):
    template_name= 'macpro.html'

# class CategoryListView(ListView):
#     model = Product
#     template_name = 'index.html'
#     context_object_name = 'categories'
#
#     def get_queryset(self):
#         # Query the database for distinct categories
#         queryset = Product.objects.values('Major_category').distinct()

#         print("Categories QuerySet:", queryset)  # Add this line for debugging
#         return queryset
#
#
