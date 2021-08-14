

from django.contrib import admin
from django.urls import path

from First_Wish_Main_App import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('addToDatabase', views.addToDatabase, name='addToDatabase'),
    path('getNames', views.getNames, name='getNames'),
    path('birthday', views.birthday, name='birthday'),

    ]
