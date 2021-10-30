from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood = models.CharField(max_length=100)

    def __str__(self):
        return self.neighbourhood

    def create_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        neighbour_hood=cls.objects.filter(neighbourhood=neighbourhood).delete()  
        return  neighbour_hood    

class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    description = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Post(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    post = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    profile_pic = CloudinaryField('image')

    def __str__(self):
        return self.title

class Comments(models.Model):
    comments = models.CharField(max_length=255)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)


class Business(models.Model):
    logo = CloudinaryField('image')
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()

    def __str__(self):
        return self.name   

    @classmethod
    def search_business(cls,search_term):
        business = cls.objects.filter(description_icontains=search_term)
        return business


class Healthservices(models.Model):
    healthservices = models.CharField(max_length=100)

    def __str__(self):
        return self.healthservices 

    def save_healthservices(self):
        self.save()

    @classmethod
    def delete_healthservices(cls,healthservices):
        cls.objects.filter(healthservices=healthservices).delete()

class Health(models.Model):
    logo = CloudinaryField('image')
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    address = models.CharField(max_length=120)
    contact = models.IntegerField()
    healthservices = models.ManyToManyField(Healthservices)

    def __str__(self):
        return self.name


class Authorities(models.Model):
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    address = models.CharField(max_length=120) 
    contact = models.ImageField()

    def __str__(self):
        return self.name       
