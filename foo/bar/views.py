from django.shortcuts import render
from django.http import HttpResponse


def newsView(request):
    return render(request, "news.html")     #from /bar/templates/news.html

def homeview(request):
    #return HttpResponse('homepage')
    return render(request, "index.html")    #from /templates/index.html, adjust /foo/settings.py, TEMPLATES, accordingly