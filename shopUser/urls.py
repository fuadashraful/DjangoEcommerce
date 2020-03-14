from django.contrib import admin
from django.urls import path,include
from . import views as userViews
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [
    #default url is 'sodai/'
    path('',userViews.HomeView,name="home") ,
    path('signup/',userViews.SignUp,name="signup"),
    path('offers/',userViews.OfferView,name="offers"),
    path('logout/',userViews.logout,name="logout"),
    path('login/',userViews.loginView,name="login"),
    path('upload_product/',userViews.productUpload,name="upload"),
    path('category/<slug>/<id>/',userViews.categoryView,name='singleCategory'),
    path('user_profile/<int:id>',userViews.ProfileView,name='profile'),
    path('user/',userViews.userProfile,name='user'),
    path('buyproduct/<categoryName>/<int:id>',userViews.buyView,name="buyproduct"),
    path('product-details/<categoryName>/<int:id>',userViews.productDetailsView,name="product_details"),

    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
