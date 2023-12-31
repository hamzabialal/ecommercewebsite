from django import forms
import stripe
from .models import ContactUs, Product, ProductImage,ShippingAddress, Reviews, Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Message'}),
        }


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30 , widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(max_length=70 , widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'form-control'}))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'in_stock',
            'warranty',
            'description',
            'price',


            'image',
            'parent',
            'is_active'
            ]


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class ExpirationDateForm(forms.Form):
    expiration_month = forms.ChoiceField(choices=[(str(month), month) for month in range(1, 13)])
    expiration_year = forms.ChoiceField(choices=[(str(year), year) for year in range(22, 31)])  # Adjust the range as needed


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            customer_id = stripe.Customer.create(
                description=self.cleaned_data['username'],
                email=self.cleaned_data['email'])
            user.stripe_Customer_id = customer_id.id
            user.save()
        return user


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['review', 'rating', 'title', 'product']
        widgets = {
            'review': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Message'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


