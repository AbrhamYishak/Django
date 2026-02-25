from django.contrib import admin
from .models import Article
class adminArticle(admin.ModelAdmin):
    list_display = ['title','content','timestamp','updated','slug']
admin.site.register(Article,adminArticle)
# Register your models here.
