from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import SignUpForm
from django.contrib import messages
from .models import CurrentOffer
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


def OfferView(request):

    if request.method=="GET":
        offerlist=CurrentOffer.objects.all()
        context={}
        context["offerlist"]=offerlist
        return render(request,'offers.html',context)