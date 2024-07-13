from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('datas',views.Datas,name='datas'),
    path('forms',views.Forms,name='forms'),

]
