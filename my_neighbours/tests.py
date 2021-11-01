from django.test import TestCase
from .models import Neighbourhood

# Create your tests here.

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.ngumba = Neighbourhood(neighbourhood='ngumba')

    def test_instance(self):
        self.assertTrue(isinstance(self.ngumba,Neighbourhood))

    def tearDown(self):
        Neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.ngumba.save_neighbourhood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.ngumba.delete_neighbourhood('ngumba')
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)
