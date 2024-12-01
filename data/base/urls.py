from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('admin/', views.admin, name="admin"),
	path('', views.home, name="home"),
    path('about-us/', views.about, name="about"),
    path('contact-us/', views.contact, name="contact"),
    path('skill/', views.skill, name="skill"),
    path('project/', views.project, name="project"),
    path('register/', views.register, name="register"),
 
	

	#CRUD PATHS

	
]