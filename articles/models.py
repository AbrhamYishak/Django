from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from .utils import slugify_article
class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True,blank=True,null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(auto_now=False,auto_now_add=False,default=timezone.now,null=True,blank=True)

def articlePreSave(instance,*args,**kwargs):
    if not instance.slug:
        slugify_article(instance)
pre_save.connect(articlePreSave,sender = Article)
# Create your models here.
