from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from .models import ProductTable

def newproduct (request):
    if request.method=='POST':
        image=request.POST.get('image')
        name=request.POST.get('name')
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')

        data=ProductTable()
        data.image=image
        data.name=name
        data.quantity=quantity
        data.price=price

        data.save()
        messages.success(request, 'New product has been added successfully.')
    return render(request,'newproduct.html')

def updateproduct (request,id):
    if request.method=='POST':
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')

        data=ProductTable.objects.get(id=id)
        data.quantity=quantity
        data.price=price
        data.save()
        messages.success(request, 'Product has been updated successfully.')
    update=ProductTable.objects.get(id=id)
    context={
        'data':update,
    }
    return render(request,'updateproduct.html',context)

def deleteproduct (request):
    data=ProductTable.objects.get(id=id)
    data.delete()
    messages.success(request, 'Product has been deleted successfully.')
    return render(request,'deleteproduct.html')

def detailsproduct (request):
    item=ProductTable.objects.all()
    context={
        'data':item,
    }
    return render(request,'detailsproduct.html',context)

def search (request):
    q=request.GET['q']
    item=ProductTable.objects.filter(name__icontains=q)
    context={
        'data':item,
    }
    return render(request,'search.html',context)
