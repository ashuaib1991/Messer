from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()

    total_customers=customers.count()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    
    context={'customers':customers, 'orders':orders, 'total_cutomers':total_customers,
    'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
    return render(request, 'dashboard.html', context)

    


def customer(request):
    return render(request,'customer.html')

def product(request):
    products=Product.objects.all()
    return render(request, 'products.html',{'products':products})

