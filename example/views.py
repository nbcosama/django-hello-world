# example/views.py
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from multiprocessing import context

from example.forms import SupplyForm
from example.models import *
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def landingpage(request):
    auth = request.user.is_authenticated
    all_data = Supply.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')  # Change 'home' to the name of your home URL pattern.
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid username or password.')
            return redirect('landingpage')
    
    context = {'all_data':all_data, 'auth':auth}
    return render(request, 'landingpage.html', context)



def signout(request):
    logout(request)
    return redirect('landingpage')




def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
        user_type = request.POST.get('role')
    
        # Convert first name to lowercase for the username
        username = first_name.lower().replace(' ', '')

        original_username = username

        try:
            # Ensure the username is unique by appending a number if necessary
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{original_username}{counter}"
                counter += 1
        
            user = User.objects.create_user(username=username, password=password)
        
            user.save()

            # Create the Buyer
            buyer = Buyer(
                first_name=first_name,
                last_name=last_name,
                email_addr=email,
                phone=phone_number,
                permanent_address=address,
                user_type = user_type,
                user_id = user.pk
            
            )
            buyer.save()

            # Create a User with the buyer's first name

            messages.success(request, "successfully added")
            return redirect('landingpage')
        except IntegrityError:
            messages.error(request, 'There was an error creating the buyer. Please try again.')
        except Exception as e:
            messages.error(request, f'An unexpected error occurred: {e}')
            return redirect('landingpage')
    return render(request, 'signup.html')





@login_required(login_url='/')
def index(request):
    user = Buyer.objects.get(user = request.user)
    products = Product.objects.all()
    cart_product = MyCart.objects.filter(added_by = user, status = "cart")
    cart_product_count = cart_product.count()
    
    
    
    if user.user_type == 'seller':
        cart_product = MyCart.objects.filter(product__added_by_id = user.id, status = "purchased")
        product_count = cart_product.count()
        purchased = MyCart.objects.filter(product__added_by_id = user.id, delivery_status = "delivered").count()
        pending = MyCart.objects.filter(product__added_by_id = user.id, delivery_status = "pending").count()
        data = {'product_count':product_count, 'pending':pending, 'purchased':purchased}
        delivered_pro = MyCart.objects.filter(product__added_by_id = user.id, delivery_status = "delivered")
        total_amount = sum(item.total_amount for item in delivered_pro)
        
        
        if request.method == 'POST':
            if request.GET.get("action") == "delivered":
                id = request.GET.get('id')
                cart_product = MyCart.objects.get(id=id)
                cart_product.delivery_status = 'delivered'
                cart_product.save()
                messages.success(request, "Product Delivered")
                return redirect('dashboard')
        context = {'user':user, 'cart_product':cart_product, 'data':data, 'total_amount':total_amount }
        return render(request, 'index.html',  context)
    else:
        if request.method == 'POST':
            if request.GET.get("action") == "addtocart":
                id = request.GET.get('id')
                cart_product = MyCart(product_id=id, added_by_id = user.id)
                cart_product.save()
                messages.success(request, "Product Added To Cart Successfully")
                return redirect('dashboard')
        context = {'user':user, 'products':products, 'cart_product_count':cart_product_count}
        return render(request, 'buyerdash.html',  context)
    
    
    
    
    

@login_required(login_url='/')
def items(request):
    user = Buyer.objects.get(user = request.user)
    if request.method == 'POST':
        product_name = request.POST.get("product_name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        file = request.FILES.get("file")
        data = Product(name=product_name,price=price, description = description, image=file, added_by_id = user.id)
        data.save()
        messages.success(request, f"{product_name} successfully added")
        return redirect('items')
            

    all_data = Product.objects.filter(added_by_id = user.id)
    context = {'all_data':all_data,}
    return render(request, 'items.html', context)


@login_required(login_url='/')
def cart(request):
    user = Buyer.objects.get(user = request.user)
    if request.method == 'POST':
        if request.GET.get("action") == "purchase":
            pid = request.GET.get('pid')
            quantity = request.POST.get('quantity')
            product_price = request.POST.get('product_price')
            total_amount = float(product_price)*int(quantity)
            cart_product = MyCart.objects.get(id=pid)
            cart_product.status = 'purchased'
            cart_product.total_amount = total_amount
            cart_product.quantity = quantity
            cart_product.totla_amount = product_price
            cart_product.save()
            messages.warning(request, "Order Placed")
            return redirect('cart')
        elif request.GET.get("action") == "delete":
            id = request.GET.get('id')
            cart_product = MyCart.objects.get(id=id)
            cart_product.delete()
            messages.warning(request, "Product Removed Successfully")
            return redirect('cart')
    
    cart_product = MyCart.objects.filter(added_by = user, status = "cart")
    cart_product_count = cart_product.count()
    context = {'user':user, 'cart_product':cart_product, 'cart_product_count':cart_product_count}
    return render(request, 'cart.html', context)