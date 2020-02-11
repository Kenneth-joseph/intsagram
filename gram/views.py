from django.shortcuts import render
from .models import Profile, Post, Comment
from django.http import HttpRequest, HttpResponse, Http404


def home(request):
    post = Post.get_post()
    return render(request, 'home.html', {"post": post})


def post(request, post_id):
    try:
        posts = Post.objects.get(id=post_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "home.html", {"posts": posts})
# Create your views here.
