from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .form import *
# Create your views here.


def HomeView(request):
    cat=PostModel.objects.all()
    posts=PostModel.objects.order_by("-create_at").filter(is_publish=True).all()[:6]
    if posts:
        posts=posts
    else:
        posts={}
    banner=BannerModel.objects.first()
    context={
        'posts':posts,
        'banner':banner,
        'cats':cat,
    }
    return render(request,'app/home.html',context)


def BlogView(request):
    post=PostModel.objects.order_by("-create_at").filter(is_publish=True).all()
    banner=BannerModel.objects.first()
    cat=PostModel.objects.all()
    context={
        'posts':post,
        'banner':banner,
        'cats':cat
    }
    return render(request,'app/blog.html',context)


def BlogDetailView(request,id):
    postDetail=PostModel.objects.filter(pk=id).first()
    comments=CommentModel.objects.filter(post=postDetail.id).all()
    print(comments)
    replys=ReplyModel.objects.all()
    print(replys)
    cat=PostModel.objects.all()
    context={
        'post':postDetail,
        'cats':cat,
        "comments":comments,
        "replys":replys
    }
    return render(request,'app/detail.html',context)


# def CategoryView(request,cat):
#     postDetail=PostModel.objects.filter(category=cat.lower()).first()
#     cat=PostModel.objects.all()
#     context={
#         'post':postDetail,
#         'cats':cat
#     }
#     return render(request,'app/detail.html',context)





def BannerDetailView(request,id):   
    cat=PostModel.objects.all()
    banner=BannerModel.objects.first()
    context={
        'banner':banner,
        'cats':cat
    }
    return render(request,'app/bannerdetail.html',context)


def AboutView(request):
    cat=PostModel.objects.all()
    context={
        'cats':cat
    }
    return render(request,'app/about.html',context)


def ContactView(request):
    cat=PostModel.objects.all()
    if request.method=='POST':
        form=ContactUsForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            redirect('/contact/')
    form=ContactUsForm()
    return render(request,'app/contact.html',{
            'form':form,
            'cats':cat
    })
    


def TotalPostView(request):
    cat=PostModel.objects.all()
    posts=PostModel.objects.filter(author=request.user).all()
    context={
        'posts':posts,
        'cats':cat
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
    user=request.user
    user_model=get_object_or_404(User,username=name)
    if request.method=='POST':
        form=UserForm(request.POST,instance=user_model)
        if form.is_valid():
            form.save()
            return redirect(f"/profile/{user}")
    form=UserForm(instance=user_model)
    return render(request,'app/profile.html',{
        "form": form,
        "user": user_model,
        "username":user,
    })


def DeleteProfileView(request,name):
    user=get_object_or_404(User,username=name)
    user.delete()
    return redirect('/')
    