from django.shortcuts import render, redirect
from .models import mainbd
from .forms import mainbdForm

def func(request):
    bd=mainbd.objects.all()
    return render(request, 'main/main.html', {'bd':bd})


def create(request):
    error=''
    if request.method=='POST':
        form=mainbdForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('about')
        else:
            error='ашипка'

    bddata=mainbd.objects.all()


    form=mainbdForm()
    data={
        'form':form,
        'error': error,
        'bddata':bddata
    }
    return render(request, 'main/create.html', data)

