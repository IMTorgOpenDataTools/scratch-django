from django.urls import path
from . import views



urlpatterns = [
    path("", views.homeview),
    path("news/", views.newsView)
]