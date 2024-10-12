from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')

def view_with_name(request, name):
    return HttpResponse(f'<h1>Hello, Mr. {name}!</h1>')

def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f'<h1> Args: {args}, kwargs: {kwargs}</h1>')

def view_with_int_pk(request, pk):
    return HttpResponse(f'<h1>Hello, ID: {pk}!</h1>')
