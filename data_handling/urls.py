from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.log),
    path('reg', views.reg),
    path('home', views.home),
    path('insert', views.insert),
    path('update/<ID>', views.update),
    path('save', views.save),
    path('delete/<ID>', views.delete),
    path('search', views.search),
    path('filter', views.filter),
    path('logout', views.logout),
]