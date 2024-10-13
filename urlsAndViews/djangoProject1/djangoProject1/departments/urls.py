from django.urls import path, include
from djangoProject1.departments import views

urlpatterns = [
    path('', views.index, name='home'),
    path('redirect/', views.redirect_to_home),
    path('softuni/', views.redirect_to_softuni),
    path('<int:pk>/', views.view_with_int_pk),
    path('<str:name>/', views.view_with_name),
    path('id/', include([
        path('<int:pk>/<slug:slug>/', views.view_with_pk_and_slug),
    ])),
    path('dp/', include([
        path('<slug:slug>/', views.view_with_slug),
    ])),
    path('<param>/', views.view_with_args_and_kwargs),
]
