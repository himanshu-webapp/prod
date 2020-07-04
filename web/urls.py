from . import views
from django.urls import path
from .feeds import BlogPostFeed

app_name = "web"

urlpatterns = [
    # # HOME
    path("", views.HomeView.as_view(), name="Home"),
    # # SERVICES
    path("services/",views.ServicesHomeView.as_view(),name="Services Home"),
    path("services/<slug:slug>",views.ServiceView.as_view(),name="Service"),
    # # CAREER
    path("career/about/",views.AboutView.as_view(),name="About"),
    path("career/jobapplication/", views.JobView.as_view(), name="Job Application"),
    path("career/certificateverification/", views.CertificateVerificationView.as_view(), name="CVF"),
    path("career/internshipapplication/", views.InternshipApplicationView.as_view(), name="Internship Application"),
    # # BLOG
    path("blog/",views.BlogHomeView.as_view(), name="Blog"),
    path("blog/<int:pk>/",views.BlogDetailView.as_view(), name="Blog Post"),
    path("blog/tags/",views.BlogTagSearchView.as_view(),name="Blog-Tag-Search"),
    path("blog/tags/<slug:slug>",views.BlogTaggedView.as_view(),name="Blog Tagged"),
    path("blog/comment/<int:pk>/", views.BlogDetailView.as_view(), name="Blog Comment"),
    path('blog/category/<str:category>',views.BlogCategoryView.as_view(),name="Blog Category"),
    # # CONTACT
    path("contact/", views.ContactView.as_view(), name="Contact"),
    # # RSS FEEDS
    path('latest/blog/feed/',BlogPostFeed(),name="Feed"),

]