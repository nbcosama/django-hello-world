# example/views.py
from datetime import datetime
from django.shortcuts import render, redirect
from multiprocessing import context

def index(request):
    now = datetime.now()
    html = 'osama'
    return render(request, 'index.html')



# def index2(request):
#     customer = Customers.objects.all()
#     count = Class.objects.count()
#     context = {
#         'customer' : customer,
#         'count' : count,   
#     }
#     return render(request, 'index2.html',context)