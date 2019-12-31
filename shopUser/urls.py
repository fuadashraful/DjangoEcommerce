from django.contrib import admin
from django.urls import path,include
from . import views as userViews
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [
 
    path('',userViews.HomeView,name="home") ,
    path('signup/',userViews.SignUp,name="signup"),
    path('offers/',userViews.OfferView,name="offers"),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 