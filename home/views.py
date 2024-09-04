from django.shortcuts import render
from django .http import HttpResponse
# Create your views here.

def home(request):
    peoples=[
        {'name':'Abhilash','age':23},
        {'name':'Abhishek','age':17},
        {'name':'Aakash','age':19},
        {'name':'Ankur','age':24},
        {'name':'Anshuman','age':25},
       
    ]
    return render(request, 'home/index.html',context={'peoples':peoples})

def success_page(request):
   return HttpResponse("<h1> Hey this is a success page <h1>")
