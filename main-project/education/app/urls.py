from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('page1/',views.about,name="about"),
     path('page2/',views.contact,name="contact"),
     path('signup/'views.form1),name='signup')
]