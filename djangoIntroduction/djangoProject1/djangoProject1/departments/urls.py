from django.urls import path
from djangoProject1.departments.views import index


urlpatterns = [
    path('', index)
]
