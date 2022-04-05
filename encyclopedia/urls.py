import imp
from django.urls import re_path,path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^wiki/(.+)/$', views.getEntry,name="entry"),
    path("search", views.search, name="search"),
    path("/random", views.getRandomEntry, name="random"),
    path("/createPage", views.createPage, name="create"),
    path("createEntry",views.createEntry,name="creatEntry"),
    re_path(r'^edit/(.+)/$', views.editPage, name="edit"),
    path("editEntry",views.editEntry,name="editEntry"),
    #path("", views.index, name="index"),
    #path("", views.index, name="index"),
]
