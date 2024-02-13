from django.http import HttpResponse


def newsView(request):
    return HttpResponse('hello')

def homeview(request):
    return HttpResponse('homepage')