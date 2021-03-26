from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def automobile(request):
    return render(request, 'automobile.html')

def construction(request):
    return render(request, 'construction.html')

def retail(request):
    return render(request, 'retail.html')
    
def smartcity(request):
    return render(request, 'customize.html')

def healthcare(request):
    return render(request, 'healthcare.html')

def upai(request):
    return render(request, "Product/UPAI.html")

def fds(request):
    return render(request, "Product/FDS.html")

def fads(request):
    return render(request, "Product/FADS.html")

def ddds(request):
    return render(request, "Product/DDDS.html")

def tds(request):
    return render(request, "Product/TDS.html")

from .models import Leads
def leads(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        information = request.POST['msg']

        lead = Leads(name=name, email=email, phone=phone, city=city, information=information )
        print(lead, name, email)
        lead.save()
        
    return redirect('index')


