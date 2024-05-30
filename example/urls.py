# example/urls.py
from django.urls import path
from . import views
from example.views import index


urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('dashboard', views.index, name='dashboard'),
    path('signup', views.signup, name='signup'),
    path('items', views.items, name='items'),
    path('signout', views.signout, name='signout'),
    path('cart', views.cart, name='cart'),
    
    
]