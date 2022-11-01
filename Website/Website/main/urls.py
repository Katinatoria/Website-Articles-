from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('articles/', views.arcan, name='articles'),
]
