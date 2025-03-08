from django.shortcuts import render,redirect
from .forms import *
# Create your views here.

def TotalPostView(request):
    return render(request,'post/totalpost.html',{})

def AddPostView(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('/post/totalpost/')
        else:
            form=PostForm()
            context={
                    'form':form
                        }
            return render(request,'post/addpost.html',context)
            
    
    form=PostForm()
    context={
    'form':form
    }
    return render(request,'post/addpost.html',context)







def EditPostView(request,pk):
    return render(request,'post/editpost.html',{})

def ProfileView(request,name):
    return render(request,'post/profile.html',{})

def EditProfileView(request,name):
    return render(request,'post/editprofile.html',{})
