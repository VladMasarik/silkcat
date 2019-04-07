from django.shortcuts import render
from django.http import HttpResponse
from blackmarket.models import Cat



def index(request):


    
    context = {}


    return HttpResponse(render(request, "bm/index.html", context))


def detail(request, id):
    out = Cat.objects.create(name="wizard", size="small", color="red", image_path="/path")
    print("#######", out, "#######")
    #cat = Cat.objects.get(id=id)

    cat = Cat()

    context = {
        "name" : cat.name,
        "size" : cat.size,
        "color" : cat.color,
        "image" : cat.image_path
    }
    return HttpResponse(render(request, "bm/detail.html", context))


def edit(request, id):
    context = {}
    return HttpResponse(render(request, "bm/edit.html", context))



def upload(request, id):
    context = {}
    return HttpResponse(render(request, "bm/upload.html", context))
