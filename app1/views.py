import imp
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Employee

# Create your views here.
def home(request):
    data=Employee.objects.all()
    return render(request,'app1/home.html',{ "Data":data})

def update(request):
    return render(request,'app1/update.html')

def signup(request):
    if(request.method == "POST"):
        e=Employee()
        e.name=request.POST.get('name')
        e.email=request.POST.get('email')
        e.salary=request.POST.get('salary')
        e.city=request.POST.get('city')
        e.state=request.POST.get('state')
        
        e.save()
        return HttpResponseRedirect("/")
    
    return render(request,'app1/signup.html')