from random import randint
from articles.models import Article
from django.template.loader import render_to_string
from django.http import HttpResponse
def home_view(request):
    articleObj = Article.objects.all()
    for i in articleObj:
        i.slug = None
        i.save()
    context = {
        "myList":articleObj
    }
    htmlString = render_to_string("home.html",context=context)
    return HttpResponse(htmlString)