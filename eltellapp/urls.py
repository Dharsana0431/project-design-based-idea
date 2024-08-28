from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('logo',views.logo,name="logo"),
    path('worker',views.worker,name="worker"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('designer',views.designer,name="designer"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('designerlogin',views.designerlogin,name="designerlogin"),
    path('marketing',views.marketing,name="marketing"),
    path('logomaking',views.logomaking,name="logomaking"),
    path('market',views.logo,name="logo"),
    path('designer',views.logo,name="logo"),
    path('service2',views.service,name="service"),

    path('reg',views.reg,name="reg"),
    path('adminview',views.adminview,name="adminview"),
    path('design',views.design,name="design"),


]
