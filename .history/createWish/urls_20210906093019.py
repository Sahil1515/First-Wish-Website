

from django.contrib import admin
from django.urls import path

from gifts import views

urlpatterns = [
    path('', views.createwish, name='createwish')

    ]
