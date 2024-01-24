from django.shortcuts import render
from.models import AboutDB

# Create your views here.

def about(request):
    data=AboutDB.objects.all()


    return render(request,'about/about.html', {'data':data})