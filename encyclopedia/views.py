from cgitb import html
from tkinter import E
from unicodedata import name
from django.shortcuts import render
import markdown
from . import util
from django.http import HttpResponse,Http404, HttpResponseNotFound
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