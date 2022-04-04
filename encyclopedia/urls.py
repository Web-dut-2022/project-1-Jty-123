import imp
from django.urls import re_path,path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^wiki/(.+)/$', views.getEntry,name="entry"),
    #path("", views.index, name="index"),
    #path("", views.index, name="index"),
    #path("", views.index, name="index"),
    #path("", views.index, name="index"),
    #path("", views.index, name="index"),
    #path("", views.index, name="index"),
]
