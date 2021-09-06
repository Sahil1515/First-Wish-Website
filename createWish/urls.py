

from django.urls import path

from createWish import views

urlpatterns = [
    path('', views.createwish, name='createwish')

    ]
