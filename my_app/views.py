from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products


# Create your views here.

def home(request):
    return HttpResponse('anything')

def index(request):
    products = Products.objects.all()
    return render(request, 'index.html', {'products': products})
    
def add_database(request):
   products = Products.objects.all()
   
   product = request.POST.get('product')
   value = request.POST.get('value')
   image = request.FILES.get('image')
   
   products = Products(
       product=product,
       value=value,
       image=image
   )
   products.save()
   return redirect('index/')