from django.urls import path
from djangoProject1.departments import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/<slug:slug>/', views.view_with_pk_and_slug),
    path('<slug:slug>/', views.view_with_slug),
    path('<int:pk>/', views.view_with_int_pk),
    path('<str:name>/', views.view_with_name),
    path('<param>/', views.view_with_args_and_kwargs),

]
