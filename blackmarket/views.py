from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    context = {}
    return HttpResponse(render(request, "bm/index.html", context))