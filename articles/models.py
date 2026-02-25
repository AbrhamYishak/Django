from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True,null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(auto_now=False,auto_now_add=False,default=timezone.now,null=True,blank=True)

def articlePreSave(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
pre_save.connect(articlePreSave,sender = Article)
def articlePostSave(*args,**kwargs):
    print(args,kwargs)
post_save.connect(articlePostSave,sender = Article)
# Create your models here.
