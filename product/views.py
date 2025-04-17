from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from .models import ProductTable, Order

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


def cart_view(request):
    orders = ProductTable.objects.all()  # You can filter by user/session if needed
    total = 0
    for item in orders:
        try:
            total += int(item.price) * int(item.quantity)
        except:
            total += 0  # fallback if quantity or price is empty or not a number

    return render(request, 'checkout.html', {'orders': orders, 'total': total})

def add_to_cart(request, product_id):
    product = get_object_or_404(ProductTable, id=product_id)
    Order.objects.create(product=product)
    return redirect('show_cart') 

def show_cart(request):
    cart_items = Order.objects.all().order_by('-added_at')
    total = 0
    for item in cart_items:
        try:
            total += int(item.price) * int(item.quantity)
        except:
            total += 0  # fallback if quantity or price is empty or not a number
    return render(request, 'billpay.html', {'cart_items': cart_items, 'total': total})

def remove_from_cart(request, order_id):
    item = get_object_or_404(Order, id=order_id)
    item.delete()
    return redirect('show_cart')