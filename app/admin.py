from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(PostModel)
admin.site.register(BannerModel)
admin.site.register(ConatactList)
admin.site.register(ContactUs)
admin.site.register(CommentModel)
admin.site.register(ReplyModel)