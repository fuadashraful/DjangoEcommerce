from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import SignUpForm,UserLoginForm,ProductForm
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

        product_name=request.POST["name"]
        present_user=request.user.id
        upload_from=request.POST["uploaded_from"]
        product_price=request.POST["price"]
        product_discount_price=request.POST["discount_price"]
        product_category=Category.objects.get(pk=request.POST["category"])
        product_description=request.POST["description"]
        product_image="product/"+request.POST["image"]
        
        print(product_category)
        obj=Product(name=product_name,uploaded_by=present_user,uploaded_from=upload_from,
        price=product_price,discount_price=product_discount_price,category=product_category,
        description=product_description,image=product_image
        )
        obj.save()

        '''
        new_product=Product(form.name,present_user,form.uploaded_from,form.price,form.discount_price,form.category,
        form.description,form.image)
        new_product.save()
        '''
        #print(request.user.id)
        return redirect('home')
    else:

        form=ProductForm()
        context["form"]=form
    return render(request,'product_upload.html',context)