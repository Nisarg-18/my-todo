from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('create',views.create,name="create"),
    path('delete/<str:id>',views.delete,name="delete"),
    path('read/<str:id>',views.read,name="read"),
    path('edit/<str:id>',views.edit,name="edit"),
]