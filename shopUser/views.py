from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import SignUpForm,UserLoginForm,ProductForm,UserForm,BuyProductForm
from django.contrib import messages,auth
from .models import CurrentOffer,Category,Product
from django.contrib.auth.models import User
# Create your views here.
# https://data-flair.training/blogs/ajax-in-django/

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

def loginView(request):

    context={}

    if request.method=="POST":
        user_form=UserLoginForm(request.POST)
 
        if user_form.is_valid():
            user=auth.authenticate(username=request.POST['username_or_email'],password=request.POST['password'])

            if user:
                auth.login(request,user)
                messages.success(request, "You have successfully logged in")
                return redirect('home')
            else:
                messages.error(request,"Your input data is not correct")

         
    else:
        user_form=UserLoginForm()
    
    context['userform']=user_form

    return render(request,'registration/login.html',context) 

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
    context={}
   
    return render(request,'offers.html',context)

def categoryView(request,slug=None,id=None):
    context={}
    if id is not None:
        category=Category.objects.get(pk=id)
        product=category.product_set.all()
        #print(product)
    context['product']=product
    return render(request,'product.html',context)

def ProfileView(request,id=None):
    context={}
    context['id']=id
    context['name']=User.objects.get(pk=id).username
    return render(request,'user_profile.html',context)

def productUpload(request):
    context={}
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.uploaded_by=request.user.id
            obj.save()
        return redirect('home')

    else:
        form=ProductForm()
        context["form"]=form
    return render(request,'product_upload.html',context)


# this is test views before appling any action
def userProfile(request):
    context={}

    if request.method=="POST":
        form=UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')

    else:
        form=UserForm()
        context["form"]=form
    return render(request,'user.html',context)


def buyView(request,categoryName=None,id=None):
    context={}
    if request.method=="POST":
        form=BuyProductForm(request.POST)
        if form.is_valid():
            order_obj=form.save(commit=False)
            order_obj.ordered_by=request.user.id
            order_obj.product_id=id
            order_obj.price=Product.objects.get(pk=id).price
            order_obj.save()
            messages.success(request, 'Your order recieved successfully thanks !') 
        return redirect('home')
    else:
        form=BuyProductForm()
        product=Product.objects.get(pk=id)
        owner=User.objects.get(pk=product.uploaded_by).username
        context['order_form']=form
        context['product']=product
        context['owner']=owner
    return render(request,'buy_product.html',context)



def productDetailsView(request,categoryName=None,id=None):
    context={}
    product=Product.objects.get(pk=id)
    owner=User.objects.get(pk=product.uploaded_by).username
    context['product']=product
    context['owner']=owner
    return render(request,'product_description.html',context)

#https://tutorial.djangogirls.org/en/django_forms/?q=