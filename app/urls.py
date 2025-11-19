from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('soma/', views.soma, name='soma'),
    path('subtracao/', views.subtracao, name='subtracao'),
    path('multiplicacao/', views.multiplicacao, name='multiplicacao'),
    path('divisao/', views.divisao, name='divisao'),
]