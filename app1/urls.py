from django.contrib import admin
from django.urls import path,include
from app1 import views


urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('projects', views.projects, name='projects'),
    path('number', views.number, name='number'),
    path('contact', views.contact, name='contact'),
    path('item_images',views.display_images,name='item_images'),
    path('success',views.success,name='success'),
    path('loginPage',views.loginPage,name="loginPage"),
    path('registerPage',views.registerPage,name="registerPage"),
    path('Choice',views.Choice,name="Choice"),
    path('sellerPage',views.sellerPage,name="sellerPage"),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('logout_view',views.logout_view,name="logout_view"),
    path('logout_view_home',views.logout_view_home,name="logout_view_home"),
]

