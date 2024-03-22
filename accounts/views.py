from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_cust = customers.count()

    ord_delivered = orders.filter(status='Delivered').count()
    ord_pending = orders.filter(status='Pending').count()
    context = {"ord_l" : orders, "cust_l": customers, "ord_count": total_orders, 
               "ord_del": ord_delivered, "ord_pend": ord_pending} 
    return render(request, 'dashboard.html', context)
def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {"list" : products})
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    cust_orders = customer.order_set.all()
    total_orders = cust_orders.count()
    context = {'cust':customer, 'cust_orders': cust_orders, "tot_ord":total_orders}
    return render(request, 'customers.html', context)