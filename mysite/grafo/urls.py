
from django.urls import path
from .views import grafo,procesaGrafo
from . import views


#app_name = 'grafo'

urlpatterns = [

    path('grafo/',grafo,name="grafo"),
    path('procesarGrafo',procesaGrafo,name="procesaGrafo")


    
]