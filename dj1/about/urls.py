from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    path('', views.about,name='about')
]
