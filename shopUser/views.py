from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import SignUpForm
from django.contrib import messages
# Create your views here.




def HomeView(request):
    return render(request,'base.html')



def SignUp(request):
    context={}

    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            messages.success(request,"User Saved")
            return redirect('home')
        else:
            messages.error(request,"Error in form")
            return redirect('signup')
    else:
        form=SignUpForm()
        context["form"]=form
    return render(request,'registration/signup.html',context)
