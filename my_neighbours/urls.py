from django.urls import path
from . import views

urlpatterns = [
    path('',views.Welcome, name='welcome'),
    # path('search/', views.search_results, name='search_results')
    path('my-profile/',views.my_profile, name='my-profile'),
    path('create-profile/',views.create_profile, name='create-profile'),
    path('profile_update/',views.updateP, name='profile_update'),
    path('posts/',views.my_post, name='posts'),
    path('new-post',views.new_post, name='new-post'), 
    path('see-post',views.see_post, name='see-post'),
]