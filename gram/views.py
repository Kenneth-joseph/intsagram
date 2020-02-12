from django.shortcuts import render, redirect
from .models import Profile, Post, Comment
from django.http import HttpRequest, HttpResponse, Http404
from .forms import NewPost
from django.contrib.auth.decorators import login_required


def home(request):
    post = Post.get_post()
    return render(request, 'home.html', {"post": post})


def post(request, post_id):
    try:
        posts = Post.objects.get(id=post_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "home.html", {"posts": posts})


# --------------------------------------------------------------------------
# define a view that calls the forms


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPost(request.POST, request.FILES)
        if form.is_valid():
            Npost = form.save(commit=False)
            Npost.profile = current_user
            Npost.save()
        return redirect('home')
    else:
        form = NewPost()
    return render(request, 'new-post.html', {"form": form})
