from django.urls import path
from djangoProject.todo_app.views import main_page, store

urlpatterns = [
    path('', main_page, name='main_page'),
    path('store/', store, name='store')
]
