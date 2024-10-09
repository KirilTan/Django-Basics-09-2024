from django.shortcuts import render
from django.http import HttpResponse

from djangoProject.todo_app.models import Task


# Create your views here.
def main_page(request):
    tasks = Task.objects.all()
    result = '\n'.join([
        '<h1>Hello, this is the main page!</h1>',
        '<ul>',
        *[f'<li>{task.name} - {task.description} - created at {task.created_at}</li>' for task in tasks],
        '</ul>',
    ])

    print(result)

    return HttpResponse(result)

def store(request):
    return HttpResponse("<h1>Hello, this is the store page!</h1>")
