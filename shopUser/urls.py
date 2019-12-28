from django.contrib import admin
from django.urls import path,include
from . import views as userViews
urlpatterns = [
 
    path('',userViews.HomeView,name="home") ,
]


