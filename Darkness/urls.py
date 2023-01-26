"""Darkness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DarknessApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parth4/display1/',views.viewdarkness,name='display1'),
    path('parth/',views.fun,name='parth'),
    path('parth1/',views.fun1,name='parth1'),
    path('parth2/',views.fun2,name='parth2'),
    path('parth5/',views.texteditor,name='parth5'),
    path('',views.fun3,name='parth3'),
    path('parth4/',views.fun4,name='parth4'),
    path('createpost/', views.createpost),
    path('blog/', views.blog),
    path('c11/', views.c1),

]
