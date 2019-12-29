from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
class SignUpForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        labels={
            'username':'Username',
            'email':'Your email',
        }
        widgets={
            'username': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'abc@gmai.com'}),
        }