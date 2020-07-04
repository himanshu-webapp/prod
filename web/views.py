# Django Imports
from django.http import HttpResponse, Http404
from django.shortcuts import render,reverse,redirect,HttpResponseRedirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template.defaultfilters import slugify
from django.contrib import messages

# Rest Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# THIRD PARTY IMPORTS
from taggit.models import Tag

# Function Imports
from . import models

# Model Imports
from .models import Contact
from blog.models import BlogPost,BlogComment
from services.models import ServiceCategory,Service,ServiceImage
from career.models import Certificate,JobApplication,InternshipApplication

# Form Imports
from .forms import ContactForm
from blog.forms import BlogCommentForm
from career.forms import CertificateVerificationForm,JobApplicationForm,InternshipApplicationForm

# Serializer Imports
from career.serializers import JobApplicationSerializer,InternshipApplicationSerializer,CertificateSerializer
from .serializers import ContactSerializer

# Global Variables
app_name = "web/"

# Global Functions
def get_category_list():
    categories = ServiceCategory.objects.all()
    category_list = []
    for cat in categories:
        services = Service.objects.filter(category=cat.slug)
        service_list = []
        for s in services:
            service_list.append({"name":s.name,"slug":s.slug})
        category_list.append({"name":cat.name,"slug":cat.slug,"services":service_list})
    return category_list
def get_categories():
    categories = BlogPost.categories_choices
    category_list = []
    for category in categories:
        category_list.append(category[1])
    return category_list

# Class Views
class HomeView(APIView):
    template_name = app_name + "home/index.html"
    form_class = ContactForm
    context = {}

    def get(self, request):
        # return JsonResponse(get_category_list(),safe=False)
        self.context["category_list"] = get_category_list()
        self.context["image_list"] = ServiceImage.objects.all()
        self.context["form"] = self.form_class
        self.context["home"] = "Home"
        # return HttpResponse(self.context)
        return render(request, self.template_name, self.context)

class ContactView(APIView):
    template_name = app_name + "others/contact.html"
    form_class = ContactForm
    context = {}
    def get(self,request):
        self.context["category_list"] = get_category_list()
        form = self.form_class
        self.context["form"] = form
        # return HttpResponse(self.context)
        return render(request,self.template_name,self.context)
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            serializer = ContactSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                serializer.save()
                messages.add_message(request, messages.SUCCESS, 'Form submitted successfully.')
            else:
                messages.add_message(request, messages.WARNING, 'Invalid form data.')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Message.')
        return HttpResponseRedirect(reverse("web:Home"))

# CAREER
class AboutView(APIView):
    template_name = app_name + "career/about.html"
    context = {}
    def get(self,request):
        self.context["category_list"] = get_category_list()
        return render(request,self.template_name,self.context)


class JobView(APIView):
    template_name = "web/career/job/index.html"
    form_class = JobApplicationForm
    model = JobApplication
    context = {}
    def get(self,request):
        self.context["category_list"] = get_category_list()
        form = self.form_class()
        self.context["form"] = form
        return render(request,self.template_name,self.context)
    def post(self,request):
        self.context["category_list"] = get_category_list()
        form = self.form_class(request.POST,request.FILES)
        # return HttpResponse(form)
        self.context["form"] = form
        if form.is_valid():
            form.save()
            messages.success(request,f'Application Successfully Submitted.')
        else:
            messages.error(request, f"Something went wrong. Are you sure you filled the form correctly")
        return render(request,self.template_name,self.context)

class InternshipApplicationView(APIView):
    template_name = "web/career/internship/index.html"
    form_class = InternshipApplicationForm
    model = InternshipApplication
    context = {}
    def get(self,request):
        self.context["category_list"] = get_category_list()
        form = self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request):
        self.context["category_list"] = get_category_list()
        form = self.form_class(request.POST,request.FILES)
        self.context["form"]=form
        if form.is_valid():
            serializer = InternshipApplicationSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                serializer.save()
                messages.success(request,f'Your form was successfully submitted. We will get back to you shortly.')
                return redirect("web:Internship Application")
            else:
                messages.error(request,f'Invalid details. Try again ...')
                return render(request,self.template_name,self.context)
        else :
            messages.error(request,f"Something went wrong. Are you sure you filled the form correctly")
            return render(request,self.template_name,self.context)

class CertificateVerificationView(APIView):
    form_class = CertificateVerificationForm
    template_name = "web/career/cvf/index.html"
    template_success = "web/career/cvf/certificate.html"
    template_failure = "web/career/cvf/404.html"
    context = {}
    def get(self,request):
        self.context["category_list"] = get_category_list()
        form = self.form_class()
        self.context = {"form":form}
        return render(request,self.template_name,self.context)

    def post(self,request):
        self.context["category_list"] = get_category_list()
        form = self.form_class(request.POST)
        if form.is_valid():
            # return JsonResponse(form.cleaned_data)
            certificateno = form.cleaned_data['certificateNo']
            dateofissue = form.cleaned_data['dateofissue']
            certificate = Certificate.objects.filter(dateofissue=dateofissue).filter(certificateno=certificateno).first()
            if certificate:
                serializer = CertificateSerializer(certificate)
                # context = {"details":serializer.data}
                details = {
                    "Certificate Number": serializer.data['certificateno'],
                    "Name": serializer.data['name'],
                    "Role": serializer.data['role'],
                    "Status": serializer.data['status'],
                    "Issued On": serializer.data['dateofissue'],
                    "Expiry On": serializer.data['dateofexpiry'],
                }
                context = {"url": serializer.data['certificateno'], "details": details,"file":certificate.certificate.url}
                return render(request,self.template_success, context)
            else:
                return render(request,self.template_failure)
        else:
            messages.error(request,f'Something went wrong! Did you fill all fields correctly? Try again...')
        return redirect("web:CVF")

# Blog View
class BlogHomeView(APIView):
    template_name = app_name + "blog/index.html"
    model = BlogPost
    context = {}

    def get(self, request):
        self.context["category_list"] = get_category_list()
        posts = BlogPost.objects.order_by("-createdon")
        self.context["searched_by"] = ""
        common_tags = self.model.tags.most_common()[:5]
        self.context["categories"] = get_categories()
        self.context["common_tags"] = common_tags
        self.context["posts"] = posts
        return render(request, self.template_name,self.context)

class BlogCategoryView(APIView):
    template_name = app_name + "blog/index.html"
    model = BlogPost
    context = {}

    def get(self,request,category):
        self.context["category_list"] = get_category_list()
        self.context["searched_by"] = category
        posts = BlogPost.objects.filter(category=category).order_by("-createdon")
        common_tags = self.model.tags.most_common()[:5]
        self.context["categories"] = get_categories()
        self.context["common_tags"] = common_tags
        self.context["posts"] = posts
        return render(request, self.template_name, self.context)


class BlogTaggedView(APIView):
    template_name = app_name + "blog/index.html"
    model = BlogPost
    context = {}
    def get(self,request,slug):
        self.context["category_list"] = get_category_list()
        tag = get_object_or_404(Tag,slug=slug)
        self.context["searched_by"] = tag.name
        posts = BlogPost.objects.filter(tags=tag)
        common_tags = self.model.tags.most_common()[:5]
        self.context["categories"] = get_categories()
        self.context["common_tags"] = common_tags
        self.context["posts"] = posts
        return render(request,self.template_name,self.context)

class BlogTagSearchView(APIView):
    template_name = app_name + "blog/index.html"
    model = BlogPost
    context = {}
    def get(self,request):
        self.context["category_list"] = get_category_list()
        name = request.GET['tag']
        tag = get_object_or_404(Tag,name=name)
        self.context["searched_by"] = tag.name
        posts = BlogPost.objects.filter(tags=tag)
        common_tags = self.model.tags.most_common()[:5]
        self.context["categories"] = get_categories()
        self.context["common_tags"] = common_tags
        self.context["posts"] = posts
        return render(request,self.template_name,self.context)

class BlogDetailView(APIView):
    template_name = app_name + "blog/post.html"
    model = BlogComment
    form_class = BlogCommentForm
    context = {}


    def get(self,request,pk):
        self.context["category_list"] = get_category_list()
        form = self.form_class
        post = BlogPost.objects.get(pk=pk)
        common_tags = BlogPost.tags.most_common()[:5]
        comments = BlogComment.objects.filter(post_id=post).order_by("-createdon")
        self.context["categories"] = get_categories()
        self.context["common_tags"] = common_tags
        self.context["comments"] = comments
        self.context["post"] = post
        self.context["form"] = form
        return render(request,self.template_name,self.context)

    def post(self,request,pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            newcomment = form.save(commit=False)
            post = BlogPost.objects.get(pk=pk)
            newcomment.post_id = post
            newcomment.save()
            return HttpResponseRedirect(reverse("web:Blog Post",kwargs={"pk":pk}))

# Services
class ServicesHomeView(APIView):
    template_name = app_name + "services/index.html"
    context = {}

    def get(self,request):
        self.context["category_list"] = get_category_list()
        return render(request,self.template_name,self.context)

class ServiceView(APIView):
    template_name = app_name + "services/service.html"
    context = {}

    def get(self,request,slug):
        self.context["category_list"] = get_category_list()
        # return HttpResponse(get_services())
        images = ServiceImage.objects.filter(category=slug)
        service = Service.objects.filter(slug=slug).first()
        if service:
            self.context["images"] = images
            self.context["service"] = service
        else:
            return HttpResponse("Service not found")
        return render(request,self.template_name,self.context)


