from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin, name='admin'),
    path('api/<int:pk>', views.About_a_company.as_view()),
    path('api/List_of_companies/', views.List_of_companies.as_view())
]