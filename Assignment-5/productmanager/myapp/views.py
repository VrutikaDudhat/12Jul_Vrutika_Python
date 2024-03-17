from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Product_mst,Product_sub_cat

# Create your views here.
def products(request):
    data=Product_sub_cat.objects.all()
    return render(request,'index.html',{'data':data})