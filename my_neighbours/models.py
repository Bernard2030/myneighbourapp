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

        
