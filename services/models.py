from django.db import models
from django.utils.text import slugify

# Create your models here.
class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(ServiceCategory,self).save(*args,**kwargs)
    def __str__(self):
        return self.name

def getcategory():
    cat = []
    obj = ServiceCategory.objects.all()
    for o in obj:
        cat.append((o.slug,o.slug))
    return cat
class Service(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200,blank=True)
    category = models.CharField(choices=getcategory(),max_length=200)
    tagline = models.CharField(max_length=200,blank=True)
    overview = models.TextField()
    body = models.TextField()
    header_image = models.ImageField(upload_to="uploads/service/header",blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Service,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

def getservices():
    ser = []
    obj = Service.objects.all()
    for s in obj:
        ser.append((s.slug,s.slug))
    return ser

class ServiceImage(models.Model):
    related_to = models.CharField(choices=getcategory(),max_length=250)
    category = models.CharField(choices=getservices(),max_length=250)
    related_to_name = models.CharField(max_length=250,blank=True)
    category_name = models.CharField(max_length=250,blank=True)
    location = models.ImageField(upload_to="uploads/service/images")
    caption = models.CharField(max_length=250,blank=True)

    def save(self,*args,**kwargs):
        self.related_to_name = ServiceCategory.objects.filter(slug=self.related_to).first().name
        self.category_name = Service.objects.filter(slug=self.category).first().name
        super(ServiceImage,self).save(*args,**kwargs)

