

from .import views
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from .views import home, update,delete

urlpatterns = [

    path('',home, name="home"),
    path('update/<int:Todo_id>/',update,name='update'),
    path('delete/<int:Todo_id>/',delete,name='delete'),

]
