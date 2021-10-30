from django.contrib import admin
from .models import Neighbourhood,Post,Profile,Comments,Business,Healthservices,Health,Authorities

# Register your models here.
admin.site.register(Profile)
admin.site.register(Neighbourhood)
admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Comments)
admin.site.register(Healthservices)
admin.site.register(Authorities)
admin.site.register(Health)