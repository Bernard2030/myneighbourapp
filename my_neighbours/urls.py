from django.urls import path
from . import views

urlpatterns = [
    path('',views.Welcome, name='welcome'),
    # path('search/', views.search_results, name='search_results')
    path('my-profile/',views.my_profile, name='my-profile'),
    path('create-profile/',views.create_profile, name='create-profile'),
    path('profile_update/',views.updateP, name='profile_update'),
    path('post',views.my_post, name='post'),
    path('new/post',views.new_post, name='new-post'), 
    path('see-post',views.see_post, name='see-post'),
    path('new-business',views.new_business, name='new-business'),
    path('business',views.businesses, name='business'),
    path('search/',views.search_results, name='search_results'),
    path('health',views.health, name='health'),
    path('authorities',views.authorities, name='authorities'),
]