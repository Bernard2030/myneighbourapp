from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from my_neighbours.forms import ProfileForm


from .models import Profile,Post,Health,User




# Create your views here.
@login_required(login_url='/accounts/login/')
def Welcome(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/account/login/')
        current_user=request.user
        # profile =Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create_profile')
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    return render(request,'user_profile.html',{'profile':profile})


@login_required(login_url='/accounts/login/')
def user_profile(request,username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(username=user)



@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')
    else:
        form = ProfileForm()
        return render(request,'profile.html',{"form":form}) 


@login_required(login_url='/accounts/login/')
def updateP(request):
    current_user = request.user
    if request.method=="POSt":
        instance = Profile.objects.get(username=current_user)
        form = ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()

        return redirect('Index')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'update_profile.html',{"form":form})    










 






