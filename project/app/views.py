from django.shortcuts import render
#from .forms import update
from .models import employee

def home(request):
    return render(request,'index.html')

def store(request):
    data=employee()

    data.name1=request.POST.get('name1')
    data.name2=request.POST.get('name2')
    data.save()
    value=employee.objects.all()
    return render (request,'base.html',{'form':value})

def show(request,id):
    user=employee.objects.get(id=id)
    
    return render(request,'edit.html',{'form':user})
def update(request,id):
    finall=employee.objects.get(id=id)
    #finall=employee()
    #finall.id=request.POST.get('id')
    finall.name1=request.POST.get('name1')
    finall.name2=request.POST.get('name2')
    finall.save()
    value=employee.objects.all()
    return render (request,'base.html',{'form':value})
