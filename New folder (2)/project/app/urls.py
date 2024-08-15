from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.Home,name='home'),
    path('register/',views.Register,name='register'),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),
    path('forms',views.Forms,name='forms'),
    path('details',views.Details,name='details'),
    path('edit/<pk>',views.Edit,name='edit'),
    path('delete/<pk>',views.Delete,name='delete'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
