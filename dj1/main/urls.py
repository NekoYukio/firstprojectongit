from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.func, name='home'),
    path('create', views.create, name='create')
]
