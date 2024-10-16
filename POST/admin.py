from django.contrib import admin
from .models import Post


# @admin.register(Post) #register the Post object in the AdminPanel

admin.site.register(Post)