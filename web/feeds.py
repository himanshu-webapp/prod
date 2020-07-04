from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import BlogPost

class BlogPostFeed(Feed):
    title = "CR-INDIA LATEST BLOG POSTS"
    link = '/blogfeeds/'
    description = "Be in touch with our latest posts"
    def items(self):
        return BlogPost.objects.order_by("-createdon")[:5]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.overview
    def item_link(self, item):
        return reverse("web:Blog Post",args=[item.pk])