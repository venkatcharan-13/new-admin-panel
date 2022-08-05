from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.resources, name='profiles'),
    path('raiseticket',views.raiseticket,name='raise_ticket')
    
]