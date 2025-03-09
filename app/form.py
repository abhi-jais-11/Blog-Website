from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import ContactUs, PostModel, CommentModel, ReplyModel


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"


class AddPostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = ["title", "author", "body", "category", "image"]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]


class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = "__all__"


class ReplyForm(ModelForm):
    class Meta:
        model = ReplyModel
        fields = "__all__"
