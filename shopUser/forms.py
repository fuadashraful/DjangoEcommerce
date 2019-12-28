from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=50,required=True,help_text="your full name")
    email=forms.EmailField(max_length=255,required=True,help_text="Inform a valid email address")
    
    class Meta:
        model=User
        fields=('username','email','password1','password2')