from cgitb import html
from pickle import NONE
from tkinter import E
from turtle import title
from unicodedata import name
from django.shortcuts import render
import markdown
from . import util
from django.http import HttpResponse,Http404, HttpResponseNotFound
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
    return HttpResponse(markdown.markdown(Entry))

def search(request):
    title = request.GET.get("q")
    Entry =util.get_entry(title)
    if Entry == None:
        return render(request,"encyclopedia/relate.html",{
            "entries":util.list_RelateEntries(title)
        })
    return HttpResponse(markdown.markdown(Entry))

def getRandomEntry(request):
    EntryList =util.list_entries()
    r = random.randint(0,len(EntryList)-1)
    Entry = util.get_entry(EntryList[r])
    return HttpResponse(markdown.markdown(Entry))