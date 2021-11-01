from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from my_neighbours.forms import BusinessForm, CommentsForm, PostForm, ProfileForm
from .models import Comments, Profile,Post,Health,User,Business,Authorities




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
    profile=Profile.objects.filter( user_id=current_user.id).first()
       
    return render(request,'user_profile.html',{'profile':profile})


@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user=request.user
    profile=Profile.objects.filter( user_id=current_user.id).first()



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
    if request.method=="POST":
        instance = Profile.objects.filter( user_id=current_user.id).first()
        form = ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()

        return redirect('/')

    elif Profile.objects.filter( user_id=current_user.id).exists():
        profile = Profile.objects.filter( user_id=current_user.id).first()
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'update_profile.html',{"form":form}) 



@login_required(login_url='/accounts/login/')
def my_post(request):
    current_user = request.user
    profile = Profile.objects.filter( user_id=current_user.id).first()
    posts = Post.objects.filter(neighbourhood=profile.neighbourhood)


    return render(request,'post.html',{'posts':posts}) 




@login_required(login_url='/accounts/login/')
def see_post(request,id):
    current_user = request.user

    try:
        comments = Comments.objects.filter(post_id=id)
    except:
        comments =[]

    my_post = Post.objects.get(id=id)
    if request.method =='POST':
        form = CommentsForm(request.POST,request.FILES)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.username = current_user
            comments.post = my_post
            comments.save()

    else:
        form = CommentsForm()
    return render(request,'see-post.html',{"my_post":my_post,"form":form,"comments":comments}) 


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user=request.user
    profile = Profile.objects.filter( user_id=current_user.id).first()


    if request.method=="POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.username = current_user
            post.neighbourhood = profile.neighbourhood
            post.profile_pic =profile.profile_pic
            post.save()

        return HttpResponseRedirect('/post')

    else:
        form = PostForm()

    return render(request,'post_form.html',{'form':form})



@login_required(login_url='/accounts/login/')
def businesses(request):
    current_user=request.user
    profile = Profile.objects.filter( user_id=current_user.id).first()
    businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)


    return render(request,'businesses.html',{"businesses":businesses}) 



@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    profile = Profile.objects.filter( user_id=current_user.id).first()


    if request.method=="POST":
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = current_user
            business.neighbourhood = profile.neighbourhood
            business.save()

        return HttpResponseRedirect('')

    else:
        form = BusinessForm()

    return render(request,'business_form.html',{"form":form}) 

@login_required(login_url='/accounts/login/')
def authorities(request):
    current_user=request.user
    profile = Profile.objects.filter( user_id=current_user.id).first()
    authorities = Authorities.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'authorities.html',{'authorities':authorities})



@login_required(login_url='/accounts/login/')
def health(request):
    current_user = request.user
    profile = Profile.objects.filter( user_id=current_user.id).first()
    healthservices = Health.objects.filter(neighbourhood=profile.neighbourhood)


    return render(request, 'health.html',{"healthservices":healthservices})



@login_required(login_url='/accounts/login/')
def search_results(request):
    current_user = request.user
    profile = Profile.objects.filter( user_id=current_user.id).first()


    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_business(search_term)
        message=f'{search_term}'

        print(searched_businesses)

    else:
        message="No term searched yet"

        return render(request,'search.html',{"message":message})        




























 






