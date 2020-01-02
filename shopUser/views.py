from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import SignUpForm
from django.contrib import messages,auth
from .models import CurrentOffer,Category
# Create your views here.




def HomeView(request):
    context={}
    offerlist=CurrentOffer.objects.all()
    categorylist=Category.objects.all()
    context["offerlist"]=offerlist
    context["categorylist"]=categorylist
    return render(request,'base.html',context)
     

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')

def SignUp(request):
    context={}

    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            user = auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password1'))
            if user:
                auth.login(request, user)
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