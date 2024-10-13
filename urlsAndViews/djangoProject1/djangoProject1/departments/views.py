from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from djangoProject1.departments.models import Department


# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')

def view_with_name(request, name):
    return render(request,'departments/name_template.html', {'name': name})

def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f'<h1> Args: {args}, kwargs: {kwargs}</h1>')

def view_with_int_pk(request, pk):
    return HttpResponse(f'<h1>Hello, ID: {pk}!</h1>')

def view_with_slug(request, slug):
    department = Department.objects.get(slug=slug)

    return HttpResponse(f'<h1> Department: {department} with slug: {department.slug}</h1>')

def view_with_pk_and_slug(request, pk, slug):
    department = get_object_or_404(Department, pk=pk, slug=slug)

    return HttpResponse(f'<h1>'
                        f'Department: {department} <br> '
                        f'slug: {department.slug}'
                        f'</h1>')

def redirect_to_softuni(request):
    return redirect('https://softuni.bg/')

def redirect_to_home(request):
    return redirect('home')
