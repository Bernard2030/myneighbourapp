from django.db import models

# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood = models.CharField(max_length=100)

    def __str__(self):
        return self.neighbourhood

    def create_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(neighbourhood=neighbourhood).delete()       

class Profile(models.Model):
    