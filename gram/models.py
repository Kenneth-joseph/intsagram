from django.db import models
import datetime as dt


class Profile(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)
    profile_pic = models.ImageField(upload_to='pictures/', default='kent')

    def save_profile(self):
        self.save()

    def __str__(self):
        return self.name


class Post(models.Model):
    content = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile)
    post_pic = models.ImageField(upload_to='pictures/', default='kent')

    def __str__(self):
        return self.content


class Comment(models.Model):
    comment = models.CharField(max_length=50)
    post = models.ForeignKey(Post)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.comment
