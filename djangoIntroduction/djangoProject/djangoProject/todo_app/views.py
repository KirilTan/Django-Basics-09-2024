from django.shortcuts import render
from django.http import HttpResponse

from djangoProject.todo_app.models import Task


# Create your views here.
def main_page(request):
    title_filter = request.GET.get('title_filter', '')

    tasks = Task.objects.filter(name__icontains=title_filter)

    context = {
        'title_filter': title_filter,
        'tasks': tasks,
    }

    return render(request, 'tasks/index.html', context)

def store(request):
    return HttpResponse("<h1>Hello, this is the store page!</h1>")
