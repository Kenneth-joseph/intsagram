from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)
    profile_pic = models.ImageField(upload_to='pictures/', default='kent')
    followers = models.IntegerField()
    following = models.IntegerField()

    def save_profile(self):
        self.save()

    def __str__(self):
        return self.name


class Post(models.Model):
    content = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    post_pic = models.ImageField(upload_to='pictures/', default='kent')
    likes = models.IntegerField()

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_post(cls):
        today = dt.datetime.today()
        post = Post.objects.all()
        return post

    def __str__(self):
        return self.content


class Comment(models.Model):
    comment = models.TextField(max_length=50)
    post = models.ForeignKey(Post)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.comment
