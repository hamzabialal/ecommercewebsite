from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from rest_framework import status

from .forms import ContactForm, SignUpForm, LoginForm, ProductForm, ShippingAddressForm, ProfileForm
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Category, ParentCategory, Cart, CartItems, Reviews, OrderTracker
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
import stripe
from django.conf import settings
from .models import Product
# Create your views here.


class Header(ListView):
    template_name = 'home.html'
    context_object_name = 'categories'

    def get_queryset(self):

        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
        parent_category_phones = ParentCategory.objects.filter(name='Phones').first()

        parent_category_tablets = ParentCategory.objects.filter(name='Tablets').first()

        if parent_category_phones:
            phones_categories = Category.objects.filter(parent_category=parent_category_phones, is_active=True)
        else:
            phones_categories = []

        context['phones'] = Product.objects.filter(
            parent__parent_category=parent_category_phones) if parent_category_phones else []
        context['tablets'] = Product.objects.filter(
            parent__parent_category=parent_category_tablets) if parent_category_tablets else []
        user = self.request.user
        if user.is_authenticated:
            cart = Cart.objects.filter(user=user, is_paid=False).first()
            if cart:
                cart_items = CartItems.objects.filter(cart=cart)
            else:
                cart_items = []
        else:
            cart_items = []

        context['cart_items'] = cart_items

        if parent_category_tablets:
            tablet_categories = Category.objects.filter(parent_category=parent_category_tablets, is_active=True)
        else:
            tablet_categories = []
        context['parent_categories'] = ParentCategory.objects.all()
        context['categories'] = Category.objects.all()
        print('It is Checkout:', context['parent_categories'])
        context['tablet_categories'] = tablet_categories
        context['phones_categories'] = phones_categories
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
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_categories'] = ParentCategory.objects.all()
        context['categories'] = Category.objects.all()
        return context


class CheckOutInfo(TemplateView):
    template_name = 'checkout_info.html'

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
        product = get_object_or_404(Product, slug=product_name)
        context['product'] = product
        context['featured_products'] = Product.objects.filter(is_featured=True)
        context['parent_categories'] = ParentCategory.objects.all()
        context['categories'] = Category.objects.all()
        context['reviews'] = Reviews.objects.filter(product=product)
        context['review_form'] = SignUpForm()
        context['additional_information'] = product.additional_information.all()
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
    success_url = '/iphonese/'

    def form_valid(self, form):
        form.save()
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
        category = get_object_or_404(Category, slug=category_name)
        products = Product.objects.filter(parent=category)
        context['category'] = category
        context['products'] = products
        context['categories'] = Category.objects.all()
        context['parent_categories'] = ParentCategory.objects.all()
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            user = self.request.user
            cart = Cart.objects.filter(user=user, is_paid=False).first()

            if cart is None:

                return redirect('checkoutcart')

            cart_items = CartItems.objects.filter(cart=cart)
            cart_total = sum(item.product.discounted_price * item.quantity for item in cart_items)

            stripe.api_key = settings.STRIPE_SECRET_KEY

            order_total = int(cart_total * 100)
            intent = stripe.PaymentIntent.create(
                amount=order_total,
                currency='usd',
                description="Example charge",
            )

            context['client_secret'] = intent.client_secret
            context['cart_total'] = cart_total
            stripe.Charge.create(
                amount=order_total,
                currency="usd",
                source="tok_amex",
                description="My First Test Charge (created for API docs at https://www.stripe.com/docs/api)",
            )
            stripe.Charge.retrieve(
                "ch_3O4HevJaQDxnEDq20n3f7bRY",
            )
            stripe.Charge.modify(
                "ch_3O4HevJaQDxnEDq20n3f7bRY",
                metadata={"order_id": "6735"},
            )

        return context


class PaymentConfirmationView(View):
    template_name = 'checkout_complete.html'

    def get(self, request):
        cart_items = request.session.get('cart_items', [])
        cart_total = sum(item.product.discounted_price * item.quantity for item in cart_items)

        request.session['cart_items'] = []

        context = {
            'cart_items': cart_items,
            'cart_total': cart_total,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        user = self.request.user

        if user.is_authenticated:
            cart = Cart.objects.filter(user=user, is_paid=False).first()
            if cart:
                cart_items = CartItems.objects.filter(cart=cart)
                cart_total = sum(item.product.discounted_price * item.quantity for item in cart_items)

                request.session['cart_items'] = []

                cart_items.delete()
                cart.is_paid = True
                cart.save()

                messages.success(request, "Payment successful. Your cart is now empty")
            else:
                cart_items = []
                cart_total = 0
        else:
            cart_items = []
            cart_total = 0

        context = {
            'cart_items': cart_items,
            'cart_total': cart_total,
        }

        return render(request, self.template_name, context)


class CheckOutCart(TemplateView):
    template_name = 'checkout_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        if user.is_authenticated:
            cart = Cart.objects.filter(user=user, is_paid=False).first()
            if cart:
                cart_items = CartItems.objects.filter(cart=cart)
                cart_total = sum(item.product.discounted_price * item.quantity for item in cart_items)
                for cart_item in cart_items:
                    cart_item.total_price = cart_item.product.discounted_price * cart_item.quantity
            else:
                cart_items = []
                cart_total = 0
        else:
            cart_items = []
            cart_total = 0

        context['cart_items'] = cart_items
        context['cart_total'] = cart_total

        return context


# def get_item_details(request):
#     item_id = request.GET.get('itemId')
#     try:
#         product = Product.objects.get(id=item_id)
#         item_data = {
#             'name': product.title,
#             'price': str(product.price),
#             'image': product.image.url,
#         }
#         return JsonResponse(item_data)
#     except Product.DoesNotExist:
#         return JsonResponse({'name': 'Item Not Found', 'price': '$Item Price', 'image': 'default-image.jpg'})

def add_to_cart(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)

    cart, created = Cart.objects.get_or_create(user=user, is_paid=False)

    cart_item, created = CartItems.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return HttpResponseRedirect(reverse('applewatch'))


def get_cart_count(self):
    count = CartItems.objects.filter(cart__is_paid=False, cart__user=self.user).count()
    print(f"Cart Count: {count}")
    return count


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'my_account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = user.profile
        cart_count = profile.get_cart_count()
        context['profile'] = profile
        context['cart_count'] = cart_count
        return context


class ProfileForms(FormView):
    template_name = 'profile.html'
    form_class = ProfileForm
    success_url = '/products/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class OrderTackeing(ListView):
    template_name = 'OrderTackeing.html'
    model = OrderTracker

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_tracker'] = OrderTracker.objects.all()
        return context


class CategoryPage(ListView):
    template_name = 'product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs['category_name']
        parent_category = get_object_or_404(Category, name=category_name)
        products = Product.objects.filter(parent=parent_category)
        context['category'] = parent_category
        context['products'] = products
        context['categories'] = Category.objects.all()
        context['parent_categories'] = ParentCategory.objects.all()
        return context


def delete_cart_item(request, product_id):
    # Assuming CartItems is the model that represents items in the cart
    cart_item = get_object_or_404(CartItems, product__id=product_id, cart__user=request.user, cart__is_paid=False)
    cart_item.delete()
    return redirect('/')

# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import re
import pickle
# import torch

from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer('stsb-distilroberta-base-v2')

# Load question embeddings
df = pd.read_csv('shope/cleaned_df.csv')
qn_embeddings = pickle.load(open('shope/distilroberta-embedding.pkl', 'rb'))


@api_view(['POST'])
def query_response(request):
    try:
        data = request.data
        query = data.get('query', '')

        if query:
            # Pre-process query
            query = re.sub(r'[^A-Za-z0-9\s]', ' ', query.lower())

            # Encode the query to get embeddings
            query_embeddings = model.encode(query).reshape(1, -1)

            # Compute similarity
            cosine_sim = cosine_similarity(qn_embeddings, query_embeddings)
            cosine_sim = [(idx, item) for idx, item in enumerate(cosine_sim)]
            sim_scores = sorted(cosine_sim, key=lambda x: x[1], reverse=True)

            # Get the index of the most similar question
            top_score = sim_scores[0]
            qn_index = top_score[0]

            # Get the corresponding answer
            response = df['answer'].iloc[qn_index]

            return Response({'response': response})
        else:
            return Response({'detail': 'Query is missing or empty'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)