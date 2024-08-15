from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.Home,name="home"),
    path('form',views.Form,name="form"),
    path('details',views.Details,name="details"),
    path('person/<pk>',views.Person,name='person'),
    path('edit/<pk>',views.Edit,name='edit'),
    path('delete/<pk>',views.Delete,name='delete'),

]