from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from .forms import ContactForm, SignUpForm, LoginForm, ProductForm,ShippingAddressForm
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import Product, Category, ParentCategory, Cart, CheckoutCart
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.shortcuts import redirect
from django.http import JsonResponse


from .models import Product



# Create your views here.

class Header(ListView):
    template_name = 'home.html'
    context_object_name = 'categories'

    def get_queryset(self):

        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Print a message to check if this method is executed.
        print("get_context_data is called")

        context['parent_categories'] = ParentCategory.objects.all()
        return context


class HomeTemplate(ListView):
    template_name = 'index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['featured_products'] = Product.objects.filter(is_featured=True)

        context['categories'] = Category.objects.all()

        parent_category = ParentCategory.objects.filter(name='Phones').first()

        if parent_category:
            context['phones'] = Product.objects.filter(parent__parent_category=parent_category)
        else:
            context['phones'] = []
        tablets_category = ParentCategory.objects.filter(name='Tablets').first()
        if tablets_category:
            context['tablets'] = Product.objects.filter(parent__parent_category=tablets_category)
        else:
            context['tablets'] = []

        context['parent_categories'] = ParentCategory.objects.all()

        return context


class FaQsTemplate(ListView):
    template_name = 'faq.html'
    context_object_name = 'categories'

    def get_queryset(self):

        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_categories'] = ParentCategory.objects.all()
        return context


class ContactTemplate(FormView):
    template_name = 'contact_us.html'
    form_class = ContactForm
    success_url = '/products/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_categories'] = ParentCategory.objects.all()
        context['categories'] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        return super(CheckOutPayment, self).get(request, *args, **kwargs)

class CheckOutInfo(TemplateView):
    template_name = 'checkout_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_categories'] = ParentCategory.objects.all()
        context['categories'] = Category.objects.all()
        return context


class CheckOutComplete(TemplateView):
    template_name = 'checkout_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_categories'] = ParentCategory.objects.all()
        context['categories'] = Category.objects.all()
        return context




class AboutUs(TemplateView):
    template_name = 'about_us.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_categories'] = ParentCategory.objects.all()
        return context


class MyAccount(TemplateView):
    template_name = 'my_account.html'


class Products(ListView):
    template_name = 'product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs['category_name']
        parent_category = get_object_or_404(ParentCategory, name=category_name)
        products = Product.objects.filter(parent__parent_category=parent_category)
        context['category'] = parent_category
        context['products'] = products
        context['categories'] = Category.objects.all()
        context['parent_categories'] = ParentCategory.objects.all()
        return context


class ProductDetail(TemplateView):
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_name = kwargs['product_name']
        product = get_object_or_404(Product, title=product_name)
        context['product'] = product
        context['featured_products'] = Product.objects.filter(is_featured=True)
        context['parent_categories'] = ParentCategory.objects.all()
        context['categories'] = Category.objects.all()
        return context






class SearchView(ListView):
    template_name = 'search_results.html'
    model = Product
    context_object_name = 'allpost'

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            queryset = self.model.objects.filter(
                Q(title__icontains=query))
        else:
            queryset = self.model.objects.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add categories to the context
        context['categories'] = Category.objects.all()

        return context


class Laptop(TemplateView):
    template_name = 'laptop.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_categories'] = ParentCategory.objects.all()
        return context


class Desktop(TemplateView):
    template_name = 'desktop.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_categories'] = ParentCategory.objects.all()
        return context


class TV(TemplateView):
    template_name = 'tv.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_categories'] = ParentCategory.objects.all()
        return context


class Speaker(TemplateView):
    template_name = 'speaker.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_categories'] = ParentCategory.objects.all()
        return context


class Gadget(TemplateView):
    template_name = 'gadget.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_categories'] = ParentCategory.objects.all()
        context['categories'] = Category.objects.all()
        return context


class RegisterForm(FormView):
    template_name = 'register.html'
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parent_category = get_object_or_404(ParentCategory, name='Phones')
        apple_category = get_object_or_404(Category, name='Apple', parent_category=parent_category)
        products = Product.objects.filter(parent=apple_category)
        context['iphone_listings'] = products
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_categories'] = ParentCategory.objects.all()
        context['categories'] = Category.objects.all()
        return context


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
    model = Product
    context_object_name = 'iphone_listings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parent_category = get_object_or_404(ParentCategory, name='Phones')
        apple_category = get_object_or_404(Category, name='Apple', parent_category=parent_category)
        products = Product.objects.filter(parent=apple_category)
        context['iphone_watch_listings'] = products
        return context


class AppleAccessories(TemplateView):
    template_name = 'appleaccessories.html'
    model = Product
    context_object_name = 'iphone_listings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parent_category = get_object_or_404(ParentCategory, name='Phones')
        apple_category = get_object_or_404(Category, name='Apple', parent_category=parent_category)
        products = Product.objects.filter(parent=apple_category)
        context['iphone_watch_listings'] = products
        return context


class MacMini(TemplateView):
    template_name = 'macmini.html'
    model = Product
    context_object_name = 'iphone_listings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parent_category = get_object_or_404(ParentCategory, name='Phones')
        apple_category = get_object_or_404(Category, name='Apple', parent_category=parent_category)
        products = Product.objects.filter(parent=apple_category)
        context['iphone_watch_listings'] = products
        return context


class MacPro(TemplateView):
    template_name = 'macpro.html'
    model = Product
    context_object_name = 'iphone_listings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parent_category = get_object_or_404(ParentCategory, name='Phones')
        apple_category = get_object_or_404(Category, name='Apple', parent_category=parent_category)
        products = Product.objects.filter(parent=apple_category)
        context['iphone_watch_listings'] = products
        return context


class AppleCategory(ListView):
    template_name = 'apple_category.html'
    model = Product
    context_object_name = 'apple_products'

    def get_queryset(self):
        return self.model.objects.filter(parent__name='Apple')


class CategoryUrl(TemplateView):
    template_name = 'apple_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = kwargs['category_name']
        category = get_object_or_404(Category, name=category_name)
        products = Product.objects.filter(parent=category)
        context['category'] = category
        context['products'] = products
        return context


class ArrivalProducts(ListView):
    template_name = 'arrivals.html'
    model = Product
    context_object_name = 'arrival_products'

    def get_queryset(self):
        return self.model.objects.filter(arrival=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_categories'] = ParentCategory.objects.all()
        context['categories'] = Category.objects.all()
        return context


class ShippingForm(FormView):
    template_name = 'checkout_info.html'
    form_class = ShippingAddressForm
    success_url = '/checkoutpayment/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CheckOutPayment(TemplateView):
    template_name = 'checkout_payment.html'


class AddToCartView(View):
    def get(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        print(product)
        if 'cart' not in request.session:
            request.session['cart'] = {}

        cart = request.session['cart']
        cart_item = cart.get(str(product_id), {'quantity': 0})
        cart_item['quantity'] += 1
        cart[str(product_id)] = cart_item
        request.session.modified = True

        return redirect('checkoutcart')

    def post(self, request, product_id):
        product = Product.objects.get(pk=product_id)

        if 'cart' not in request.session:
            request.session['cart'] = {}

        cart = request.session['cart']
        cart_item = cart.get(str(product_id), {'quantity': 0})
        cart_item['quantity'] += 1
        cart[str(product_id)] = cart_item
        request.session.modified = True
        return redirect('checkoutcart')


class CheckOutCart(TemplateView):
    template_name = 'checkout_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart = self.request.session.get('cart', {})

        item_total = {}
        cart_total = 0

        for product_id, cart_item in cart.items():
            try:
                product = Product.objects.get(pk=product_id)
                item_total[product_id] = cart_item['quantity'] * product.price
                cart_total += item_total[product_id]
                cart_item['product'] = product
                cart_item['total_price'] = item_total[product_id]
            except Product.DoesNotExist:
                cart_item['product'] = None
                cart_item['total_price'] = 0

        context['cartitems'] = cart.values()
        context['cart_total'] = cart_total

        return context


def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})
    cart_item = cart.get(str(product_id))

    if cart_item and cart_item['quantity'] < 10:  # Check if the quantity is less than 10
        cart_item['quantity'] += 1
        request.session['cart'] = cart

    return redirect('checkoutcart')

def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})
    cart_item = cart.get(str(product_id))

    if cart_item and cart_item['quantity'] > 1:  # Check if the quantity is greater than 1
        cart_item['quantity'] -= 1
        request.session['cart'] = cart

    return redirect('checkoutcart')


def get_item_details(request):
    item_id = request.GET.get('itemId')
    try:
        product = Product.objects.get(id=item_id)
        item_data = {
            'name': product.title,
            'price': str(product.price),
            'image': product.image.url,
        }
        return JsonResponse(item_data)
    except Product.DoesNotExist:
        return JsonResponse({'name': 'Item Not Found', 'price': '$Item Price', 'image': 'default-image.jpg'})
# class CheckoutCart(ListView):
#     model = CheckoutCart
#     template_name = 'checkout_cart.html'
#
#
#     def post(self, request, *args, **kwargs):
#         product_id = request.POST.get('prod_id')
#         operation = request.POST.get('operation')
#         operation1 = request.POST.get('operation1')
#         pro_check = CheckoutCart.objects.filter(product_id=product_id, user=request.user)
#         if pro_check.exists():
#             cart = CheckoutCart.objects.filter(product_id=product_id).first()
#             if operation == 'decrease':
#                 cart.quantity -= 1
#                 cart.save()
#                 if cart.quantity == 0:
#                     cart.delete()
#             elif operation1 == 'increase':
#                 cart.quantity += 1
#                 cart.save()
#
#             else:
#                 cart.quantity += 1
#                 cart.save()
#
#         else:
#             cart_item = CheckoutCart.objects.create(product_id=product_id, user=request.user)
#             cart_item.save()
#         product_show = CheckoutCart.objects.all()
#
#         shipping = 10
#         sub_total = 0
#         total = 0
#         for item in product_show:
#             if item.product:
#                 item.pro_total = item.quantity * item.product.price
#                 sub_total += item.pro_total
#                 total = (sub_total + shipping)
#                 item.save()
#         context = {
#             'product_show': product_show,
#             'sub_total': sub_total,
#             'total': total,
#
#         }
#         return render(request, self.template_name, context)

