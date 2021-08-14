

from django.contrib import admin
from django.urls import path

from addPerson import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.addPerson),
    path('add_person_api', views.add_person_api, name='add_person_api')

    # path('personAdded', views.personAdded, name='personAdded')
    
    ]
