from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Product,UserProfile,Order
from django.forms import ModelForm
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
class SignUpForm(UserCreationForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Re-password',
        widget=forms.PasswordInput
    )
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2


class UserLoginForm(forms.Form):
    '''
    this form use for login account
    '''
    username_or_email=forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)


class ProductForm(ModelForm):
    
    class Meta:
        model=Product
        #fields='__all__'
         
        fields=['name','uploaded_from','price',
        'discount_price','category','description',
        'image',
        ]

class UserForm(ModelForm):

    class Meta:
        model=UserProfile
        fields='__all__'


class BuyProductForm(ModelForm):
    
    class Meta:
        model=Order
        fields=['location','contact','transection_no','payment_method']