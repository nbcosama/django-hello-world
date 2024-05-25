# example/views.py
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from multiprocessing import context

from example.forms import SupplyForm
from example.models import *

def index(request):
    now = datetime.now()
    html = 'osama'
    all_data = Supply.objects.all()
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supply created successfully.')
            return redirect('index')  # Redirect to a success page
    else:
        form = SupplyForm()
    context = {'all_data':all_data, 'form': form}
    return render(request, 'index.html',  context)



# def index2(request):
#     customer = Customers.objects.all()
#     count = Class.objects.count()
#     context = {
#         'customer' : customer,
#         'count' : count,   
#     }
#     return render(request, 'index2.html',context)