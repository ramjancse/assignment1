from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1> Home page from django</h1>')

def about(request):
    return HttpResponse('about page')

def service(request):
    return HttpResponse('service page')

def contact(request):
    return HttpResponse('contact page')