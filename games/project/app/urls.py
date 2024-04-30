
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Specify the view function for the root URL
    # path('base/', views.base, name='base'),
    path('page/', views.page, name='page'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.authlogin, name='login'),
    path('logout/', views.logout, name='logout')
]
