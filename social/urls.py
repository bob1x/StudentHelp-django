from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # assuming 'index' is the view you want to route to

 #  
]