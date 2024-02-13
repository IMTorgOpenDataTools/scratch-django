from django.shortcuts import render
from django.http import HttpResponse


def newsView(request):
    return render(request, "news.html")

def homeview(request):
    return HttpResponse('homepage')