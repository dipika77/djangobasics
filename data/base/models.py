from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class home(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200, blank=True, null=True)
	last_name = models.CharField(max_length=200, blank=True, null=True)
	email = models.CharField(max_length=200)
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images", default="/user.png")
	bio = models.TextField(null=True, blank=True)
	twitter = models.CharField(max_length=200,null=True, blank=True)
 
 
class Registers(models.Model):
    name = models.CharField(max_length=200)
