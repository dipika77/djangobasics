from django.shortcuts import render
from django.http import HttpResponse
from folder.models import models

# Create your views here.
# def home(request):
#     folder = models.objects.all()             
#     print(folder)
#     template_name = 'index.html'
#     context = {
#         'posts': folder
#     }
def home(request):
     return render(request, 'templates/index.html')
def keep(request):
  return HttpResponse("welcome to keep page")



