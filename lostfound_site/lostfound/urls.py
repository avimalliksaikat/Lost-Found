from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-lost/', views.add_lost, name='add_lost'),
    path('add-found/', views.add_found, name='add_found'),
    path('view/', views.view_items, name='view_items'),
    path('search/', views.search_items, name='search_items'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('my-items/', views.my_items, name='my_items'),
]