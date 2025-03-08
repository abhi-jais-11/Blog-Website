from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import  ContactUs,PostModel
class ContactUsForm(ModelForm):
    class Meta:
        model=ContactUs
        fields='__all__'
        

class AddPostForm(ModelForm):
    class Meta:
        model=PostModel
        fields=['title','author','body','category','image']
        