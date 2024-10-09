from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_page(request):
    return HttpResponse("<h1>Hello, this is the main page!</h1>")

def store(request):
    return HttpResponse("<h1>Hello, this is the store page!</h1>")
