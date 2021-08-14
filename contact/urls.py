
from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('contact',views.contact,name='contact'),
    path('send_mail_by_user',views.send_mail_by_user,name='send_mail_by_user'),

]