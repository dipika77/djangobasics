from django.shortcuts import render
from django.http import HttpResponse
from .models import Registers

# Create your views here.
def admin(request):
    return render(request)
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def project(request):
    return render(request, 'project.html')

def skill(request):
    return render(request, 'skill.html')

def register(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        obj = Registers(name=name)
        obj.save()
        return HttpResponse('data received')
    return render(request, 'register.html')






