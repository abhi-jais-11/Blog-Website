from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .form import *
# Create your views here.


def HomeView(request):
    posts=PostModel.objects.order_by("-create_at").filter(is_publish=True).all()[:6]
    if posts:
        posts=posts
    else:
        posts={}
    banner=BannerModel.objects.first()
    context={
        'posts':posts,
        'banner':banner
    }
    return render(request,'app/home.html',context)


def BlogView(request):
    post=PostModel.objects.order_by("-create_at").filter(is_publish=True).all()
    banner=BannerModel.objects.first()
    context={
        'posts':post,
        'banner':banner
    }
    return render(request,'app/blog.html',context)


def BlogDetailView(request,id):
    postDetail=PostModel.objects.filter(pk=id).first()
    context={
        'post':postDetail,
    }
    return render(request,'app/detail.html',context)

def BannerDetailView(request,id):
    banner=BannerModel.objects.first()
    context={
        'banner':banner
    }
    return render(request,'app/bannerdetail.html',context)


def AboutView(request):
    context={}
    return render(request,'app/about.html',context)


def ContactView(request):
    if request.method=='POST':
        form=ContactUsForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            redirect('/contact/')
    form=ContactUsForm()
    return render(request,'app/contact.html',{
            'form':form
    })
    


def TotalPostView(request):
    posts=PostModel.objects.all()
    context={
        'posts':posts
    }
    return render(request,'app/totalpost.html',context)


def AddPostView(request):
    if request.method=='POST':
        form=AddPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=AddPostForm()
    return render(request,'app/addpost.html',{
        "form":form
    })


def EditPostView(request,pk):
    post=get_object_or_404(PostModel,pk=pk)
    if request.method=='POST':
        form=AddPostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('/totalpost/')
    form=AddPostForm(instance=post)
    return render(request,'app/editpost.html',{
        "form": form,
        "post": post  
    })
 

def DeletePostView(request,id):
    post=get_object_or_404(PostModel,pk=id)
    post.delete()
    return redirect('/totalpost/')
    
def ProfileView(request,name):
    return render(request,'app/profile.html',{})

def EditProfileView(request,name):
    return render(request,'app/editprofile.html',{})
