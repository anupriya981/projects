from django.urls import path
from .import views

urlpatterns = [
   
    path('',views.base,name='base'),
    path('login',views.User_login,name='login'),
    path('signUp',views.User_signUp,name='signUp'),
    path('logout',views.User_logout,name='logout')
]