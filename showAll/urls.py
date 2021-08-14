

from django.contrib import admin
from django.urls import path

from showAll import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.showAll),

    ]