from cgitb import html
from pickle import NONE
from tkinter import E
from turtle import title
from unicodedata import name
from django.shortcuts import render
import markdown
from . import util
from django.http import HttpResponse,HttpResponseNotFound
import random
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def getEntry(request,param):
    title  = param
    Entry =util.get_entry(title)
    if Entry == None:
        return HttpResponseNotFound("Sorry,You request page is not found!")
    return render(request, "encyclopedia/show.html", {
        "Title":title,
        "Entry":markdown.markdown(Entry)
    })

def search(request):
    title = request.GET.get("q")
    Entry =util.get_entry(title)
    if Entry == None:
        return render(request,"encyclopedia/relate.html",{
            "entries":util.list_RelateEntries(title)
        })
    return render(request, "encyclopedia/show.html", {
        "Title":title,
        "Entry":markdown.markdown(Entry)
    })

def getRandomEntry(request):
    EntryList =util.list_entries()
    r = random.randint(0,len(EntryList)-1)
    Entry = util.get_entry(EntryList[r])
    return render(request, "encyclopedia/show.html", {
        "Title":title,
        "Entry":markdown.markdown(Entry)
    })

def createPage(request):
    return render(request, "encyclopedia/create.html")

def createEntry(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    Entry = util.get_entry(title)
    if Entry is not None:
        return HttpResponse("Error,the Entry already exists!")
    util.save_entry(title, content)
    Entry = util.get_entry(title)
    return render(request, "encyclopedia/show.html", {
        "Title":title,
        "Entry":markdown.markdown(Entry)
    })

def editPage(request,param):
    title  = param
    Entry =util.get_entry(title)
    return render(request, "encyclopedia/edit.html",{
        "Title":title,
        "Content":Entry
    })
def editEntry(request):
    content = request.GET.get("content")
    title= request.GET.get("title")
    util.save_entry(title, content)
    Entry = util.get_entry(title)
    return render(request, "encyclopedia/show.html", {
        "Title":title,
        "Entry":markdown.markdown(Entry)
    })