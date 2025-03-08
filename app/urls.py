from django.urls import path
from .views import *

app_name='app'

urlpatterns = [
    path('',HomeView,name='home'),
    path('blog/',BlogView,name='blog'),
    path('detail/<int:id>',BlogDetailView,name='detail'),
    path('banner/<int:id>',BannerDetailView,name='banner'),
    path('about/',AboutView,name='about'),
    path('contact/',ContactView,name='contact'),
    path('totalpost/',TotalPostView,name="totalpost"),
    path('add-post/',AddPostView,name="addpost"),
    path('edit-post/<int:pk>',EditPostView,name="editpost"),
    path('profile/<str:name>',ProfileView,name="profile"),
    path('edit-profile/<str:name>',EditProfileView,name="editprofile"),
    path('delete-post/<int:id>',DeletePostView,name="deletepost"),
    # path('delete-profile/<str:name>'),
]