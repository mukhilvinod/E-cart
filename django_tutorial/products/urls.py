from django.urls import path,re_path
from . import views


urlpatterns = [
    path('',views.dummy),
    re_path('new_reg/',views.register,name='register'),
    re_path('login/',views.login,name='login'),
    path('index',views.index,name='index'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('connect',views.connect, name='connect')
    
    
]

