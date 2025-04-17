from django.shortcuts import render,redirect
from django.contrib import messages
#from .models import ProductTable
from product.models import ProductTable
from .models import Order
# Create your views here.
def billpay (request,id):
        data=ProductTable.objects.get(id=id)
        return render(request,'billpay.html',{"product":data})


def checkout (request):
        messages.success(request, 'Payment successfull.')
        return render(request,'checkout.html',)
