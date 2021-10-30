from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,BusinessForm,CommentsForm,PostForm
from django.http import HttpResponse, Http404,HttpResponseRedirect

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
    return render(request,'user_profile.html',{"profile":profile}) 

# @login_required(login_url='/accounts/login/')
# def user_profile(request,username):
#     user = User.objects.get(username=username)
#     profile = Profile.objects.get(username=user) 






# def search_results(request):

#     if 'article' in request.GET and request.GET["article"]:
#         search_term = request.GET.get("article")
#         searched_articles = Article.search_by_title(search_term)
#         message = f"{search_term}"

#         return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'all-news/search.html',{"message":message})  
# 





