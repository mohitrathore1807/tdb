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

def heartrate(request):
    return render(request, "Product/Heartrate.html")

from .models import Leads
def leads(request):
    name = request.POST.get('FirstName', False)
    email = request.POST.get('Email', False)
    phone = request.POST.get('Phone', False)
    company = request.POST.get('Company', False)
    inquiry_type = request.POST.get('enquiry', False)
    helping = request.POST.get('howcanwehelptextarea', False)
    print(name, email, phone)

    lead = Leads(name=name, email=email, phone=phone, company=company, inquiry_type=inquiry_type, helping=helping )

    lead.save()
        
    return redirect('index')

from .models import Post
def blog(request):
    post = Post.objects.all()
    

    return render(request, 'blog.html', {'post': post})


def post(request, id):
    post1 = Post.objects.filter(title=id).first()

    return render(request, 'post.html', {'post': post1})

def sitemap(request):
    
    return render(request, "sitemap.xml", content_type='application/xml')

def robots(request):
    return render(request, "robots.txt")

