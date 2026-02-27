from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Article
from .forms import articleForm
def article_detail_view(request,slug = None):
    artObj = None
    if slug is not None:
        try:
            artObj = Article.objects.get(slug = slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            artObj = Article.objects.filter(slug = slug).first()
        except:
            raise Http404
    context = {
        "object" : artObj,
    }
    return render(request,"articles/detail.html",context = context)
def article_search_view(request):
    query = None
    if "query" in request.GET:
        query = request.GET["query"]
        try:
            query = int(query)
        except:
            query = None
    objArt = None
    if query:
        objArt = Article.objects.get(id = query)
    context = {
        "object":objArt
    }
    return render(request,"articles/search.html",context=context)
@login_required
def article_create_view(request):
    form = articleForm(request.POST or None)
    context = {
        "form": form
    }
    if request.POST:
        if form.is_valid():
            ObjArt = form.save()
            context["form"] = articleForm()
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # ObjArt = Article.objects.create(title=title,content=content)
            context["object"] = ObjArt
            context["success"] = True 
    return render(request,"articles/create.html",context = context)
# Create your views here.
