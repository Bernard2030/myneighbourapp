from django.shortcuts import render


# Create your views here.
def Welcome(request):
    return render(request, 'welcome.html')