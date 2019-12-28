from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SignUpForm
# Create your views here.




def HomeView(request):
    return render(request,'base.html')



def SignUp(request):
    context={}

    if request.method=="POST:
        form=SignUpForm(request.POST)
    
    else:
        form=SignUpForm()
        context["form"]=form
    return render(request,'registration/signup.html',context)
