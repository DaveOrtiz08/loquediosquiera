from django.contrib import admin
from django.urls import path
from .views import home
from . import views

app_name = 'home'

urlpatterns = [

    path('',home,name="home"),

    
]