from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_POST
from django.shortcuts import render
from .models import Order
from .models import OrderItem
from .forms import OrderCreateForm
from .forms import OrderGetForm
from cart.cart import Cart
from cart.forms import CartAddProductForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
@csrf_exempt
def order_registerButton1(request, order_id):
    if request.method=='POST':
        url='http://127.0.0.1:8001/registerbutton1/lcy32/' + order_id+'/'
        r = requests.get(url)
        print(r.status_code)
        return HttpResponse("Order registered to button 1!")
    return render(request, 'orders/order/created.html', {'order': order_id})

@csrf_exempt
def order_registerButton2(request, order_id):
    if request.method=='POST':
        url='http://127.0.0.1:8001/registerbutton2/lcy32/' + order_id+'/'
        r = requests.get(url)
        print(r.status_code)
        return HttpResponse("Order registered to button 2!")
    return render(request, 'orders/order/created.html', {'order': order_id})

    
@csrf_exempt
def order_registerButton3(request, order_id):
    if request.method=='POST':
        url='http://127.0.0.1:8001/registerbutton3/lcy32/' + order_id+'/'
        r = requests.get(url)
        print(r.status_code)
        return HttpResponse("Order registered to button 3!")
    return render(request, 'orders/order/created.html', {'order': order_id})

@csrf_exempt
def order_registerButton4(request, order_id):
    if request.method=='POST':
        url='http://127.0.0.1:8001/registerbutton4/lcy32/' + order_id+'/'
        r = requests.get(url)
        print(r.status_code)
        return HttpResponse("Order registered to button 4!")
    return render(request, 'orders/order/created.html', {'order': order_id})

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})

    
def order_view(request, order_id):
    cart = Cart(request)
    cart.removeall()
    order = get_object_or_404(Order, order_id=order_id)
    orderitems = get_list_or_404(OrderItem, order_id=order.id)
    for orderitem in orderitems:
        cart.add(orderitem.product, orderitem.quantity)
    cart.save()
    return redirect('cart:cart_detail')

@csrf_exempt    
def order_reorder(request, order_id):
    #cart = Cart(request)
    #if request.method == 'POST':
    #    cart.removeall()
    #    order = get_object_or_404(Order, order_id=order_id)
    #    orderitems = get_list_or_404(OrderItem, order_id=order.id)
    #    for orderitem in orderitems:
    #        cart.add(orderitem.product, orderitem.quantity)
    #    cart.save()
    #    order_create(request)
    #    return render(request, 'orders/order/created.html', {'order': order})
    #return redirect('cart:cart_detail')
    cart = Cart(request)
    cart.removeall()
    order = get_object_or_404(Order, order_id=order_id)
    orderitems = get_list_or_404(OrderItem, order_id=order.id)
    for orderitem in orderitems:
        cart.add(orderitem.product, orderitem.quantity)
    cart.save()
    neworder=Order()
    neworder.first_name = order.first_name
    neworder.last_name = order.last_name
    neworder.email = order.email
    neworder.address = order.address
    neworder.postal_code = order.postal_code
    neworder.city = order.city
    neworder.save()
    for item in cart:
        OrderItem.objects.create(
            order=neworder,
            product=item['product'],
            price=item['price'],
            quantity=item['quantity']
        )
    cart.clear()
    return render(request, 'orders/order/created.html', {'order': neworder})



@csrf_exempt
def order_default(request):
        return HttpResponse( content_type = "application/json", status_code = 200)
@csrf_exempt
def order_button_api(request, order_id):
    if request.method == 'GET':
        text = """<h1>Your order id is </h1>""" + order_id
        return HttpResponse(text)
    if request.method == 'POST' :
        cart = Cart(request)
        cart.removeall()
        order = Order.get_object_or_404(Order, order_id=order_id)
        orderitems = get_list_or_404(OrderItem, order_id=order.id)
        for orderitem in orderitems:
            cart.add(orderitem.product, orderitem.quantity)
        cart.save()
        neworder=Order()
        neworder.first_name = order.first_name
        neworder.last_name = order.last_name
        neworder.email = order.email
        neworder.address = order.address
        neworder.postal_code = order.postal_code
        neworder.city = order.city
        neworder.save()
        for item in cart:
            OrderItem.objects.create(
                order=neworder,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        return HttpResponse("Order placed")
    return HttpResponse( content_type = "application/json", status_code = 200)