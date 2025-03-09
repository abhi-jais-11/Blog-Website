from .models import *

def CatData():
    cat = PostModel.objects.all() 
    return cat

def HomeData():
    posts = PostModel.objects.order_by("-create_at").filter(is_publish=True).all()[:6]
    banner = BannerModel.objects.first()
    cat = CatData()
   

    return posts, banner, cat


def BannerDetailData():
    banner = BannerModel.objects.first()
    cat = CatData()

    return banner, cat


def BlogData():
    post = PostModel.objects.order_by("-create_at").filter(is_publish=True).all()
    banner = BannerModel.objects.first()
    cat = CatData()

    return post, banner, cat


def BlogDetailData(id):
    postDetail = PostModel.objects.filter(pk=id).first()
    comments = CommentModel.objects.filter(post=postDetail.id).all()
    replys = ReplyModel.objects.all()
    cat = CatData()

    return postDetail, comments, replys, cat


def AboutData():
    abouts = AboutUs.objects.all()
    about_single = abouts[0]
    our_story = abouts[1]
    our_mission = abouts[2]
    aboutcards = AboutList.objects.all()
    cat = CatData()

    return about_single, our_story, our_mission, aboutcards, cat


def ContactData():
    cat = CatData()
    contacts = ConatactList.objects.all()

    return contacts, cat


def TotalPostData(user):
    cat = CatData()
    posts = PostModel.objects.filter(author=user).all()

    return posts, cat
