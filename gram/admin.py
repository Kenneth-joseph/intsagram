from django.contrib import admin
from .models import Comment, Profile, Post

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Profile)
