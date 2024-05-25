# example/urls.py
from django.urls import path
from . import views
from example.views import index


urlpatterns = [
    path('', views.index, name='index'),
]