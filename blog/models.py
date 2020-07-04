from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    tags = TaggableManager()
    overview = models.TextField()

    categories_choices = [("Educate", "Educate"), ("News & Media", "News & Media"), ("Seminars", "Seminars"), ("Case Studies", "Case Studies"),
                          ("Articles", "Articles")]

    category = models.CharField(choices=categories_choices,default="Articles",max_length=50)
    body = models.TextField(default="Welcome")
    allowcomments = models.BooleanField(default=True)
    noofcomments = models.IntegerField(default=0)
    createdon = models.DateTimeField(auto_now=timezone)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['createdon']

class BlogComment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    is_approved = models.BooleanField(default=True)
    createdon = models.DateTimeField(auto_now_add=True)
    post_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.email)

