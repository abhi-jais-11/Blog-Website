from django.shortcuts import render, redirect, get_object_or_404
from .models import PostModel
from .form import *
from .db_query import *

# Create your views here.


def HomeView(request):
    posts, banner, cat = HomeData()
    context = {
        "posts": posts,
        "banner": banner,
        "cats": cat,
    }
    return render(request, "app/home.html", context)


def BlogView(request):
    posts, banner, cat = BlogData()
    context = {"posts": posts, "banner": banner, "cats": cat}
    return render(request, "app/blog.html", context)


def BlogDetailView(request, id):
    postDetail, comments, replys, cat = BlogDetailData(id)
    context = {"post": postDetail, "cats": cat, "comments": comments, "replys": replys}
    return render(request, "app/detail.html", context)


def BannerDetailView(request):
    banner, cat = BannerDetailData()
    context = {"banner": banner, "cats": cat}
    return render(request, "app/bannerdetail.html", context)


def AboutView(request):
    about_single, our_story, our_mission, aboutcards, cat = AboutData()
    context = {
        "cats": cat,
        "about_single": about_single,
        "our_story": our_story,
        "our_mission": our_mission,
        "cards": aboutcards,
    }
    return render(request, "app/about.html", context)


def ContactView(request):
    contacts, cat = ContactData()
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            redirect("/contact/")
    form = ContactUsForm()
    return render(
        request, "app/contact.html", {"form": form, "cats": cat, "contacts": contacts}
    )


def TotalPostView(request):
    posts, cat = TotalPostData(request.user)
    context = {"posts": posts, "cats": cat}
    return render(request, "app/totalpost.html", context)


def AddPostView(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    form = AddPostForm()
    return render(request, "app/addpost.html", {"form": form})


def EditPostView(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("/totalpost/")
    form = AddPostForm(instance=post)
    return render(request, "app/editpost.html", {"form": form, "post": post})


def DeletePostView(request, id):
    post = get_object_or_404(PostModel, pk=id)
    post.delete()
    return redirect("/totalpost/")


def ProfileView(request, name):
    user = request.user
    user_model = get_object_or_404(User, username=name)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user_model)
        if form.is_valid():
            form.save()
            return redirect(f"/profile/{user}")
    form = UserForm(instance=user_model)
    return render(
        request,
        "app/profile.html",
        {
            "form": form,
            "user": user_model,
            "username": user,
        },
    )


def DeleteProfileView(request, name):
    user = get_object_or_404(User, username=name)
    user.delete()
    return redirect("/")
