from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import BuyerTable,Report

# Create your views here.
def home (request):
    title='Billing Management System'
    desc="""We offer an efficient, project-based billing management system that
    supports multiple revenue streams, simplified recurring revenue and payment
    gateways. It aims at reducing key constraints like billing errors, customer
    attrition, revenue recognition issues and instant workload.
    Our experts provide invoicing solutions that are easy and convenient, translating
    the system into a modest asset for an organization by fully integrating it into its
    existing billing mechanism.
    Our developers provide innovative billing solution to systematize complex calculations
    so as to simplify the key elements of an accounting process. With its high degree of
    automation, the billing software minimizes overhead expenses and significantly improves productivity."""
    context={
        'title':title,
        'description':desc
    }
    return render(request,'index.html',context)

def newbuyer (request):
    return render(request,'newbuyer.html')

def updatebuyer (request):
    return render(request,'updatebuyer.html')

def deletebuyer (request,id):
    user=User.objects.get(id=id)
    user.delete()
    context={
        'data':user
    }
    messages.success(request, 'Buyer has been deleted successfully.')
    return render(request,'deletebuyer.html',context)

def buyerdetails (request):
    buyer=User.objects.all()
    context={
        'data':buyer,
    }
    #buyer_tab=BuyerTable.objects.all()
    #context={
    #    'data':buyer_tab,
    #}
    return render(request,'buyerdetails.html',context)

def contact (request):
    if request.method=='POST':
    #to get data from design templates
        username=request.POST.get('username')
        email=request.POST.get('email')
        desc=request.POST.get('comments')

        #to pass data into model (method=1)
        data=Report(username=username,email=email,desc=desc)
        #to pass data into model (method=2)
        # data=Report()
        # data.username=username
        # data.email=email
        # data.desc=desc

        #to save data
        data.save()
    return render(request,'contact.html')

# def all_messages(request):
#         msg=Report.objects.all()
#         context={
#             'data':msg,
#         }
#     return render(request,'all_msg.html',context)
