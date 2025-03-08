from django.urls import path
from .views import *


app_name='post'

urlpatterns = [
    path('',TotalPostView,name="totalpost"),
    path('add-post/',AddPostView,name="addpost"),
    path('edit-post/<int:pk>',EditPostView,name="editpost"),
    # path('delete-post/<int:pk>',),
    path('profile/<str:name>',ProfileView,name="profile"),
    path('edit-profile/<str:name>',EditProfileView,name="editprofile"),
    # path('delete-profile/<str:name>'),
    
]