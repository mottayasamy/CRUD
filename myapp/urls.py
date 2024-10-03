from django.urls import path
from . import views

urlpatterns = [
    path('createtab/', views.create1, name='createtab'),
    path('readtab/', views.read, name='readtab'),
    path('<int:pk>/updatetab/', views.update, name='updatetab'),
    path('<int:pk>/deletetab/', views.delete, name='deletetab'),
]
