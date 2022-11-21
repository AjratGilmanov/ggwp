"""Gilmanov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Ajrat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.info,kwargs = {'name':'Айрат', 'age':'16' }),
    path('about',views.about,kwargs = {'From':'Нижнекамск', 'uspev':'Нормас','stlo':'Люблю конечно'}),
    path('contact',views.contact, kwargs = {'Tg': "@AjratGilmanov",'tel':'8-909-314-49-83','Github':'https://github.com/AjratGilmanov'})
]
