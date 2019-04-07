from django.shortcuts import render
from django.http import HttpResponse
from blackmarket.models import Cat



def index(request):

    #cat = Cat.objects.create(name="wizard", size="small", color="red", image_path="/path")

    
    context = {}


    return HttpResponse(render(request, "bm/index.html", context))


def detail(request, id):

    cat = Cat.objects.get(id=id)

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


def delete(request, id):
    Cat.objects.get(id=id).delete()
    return HttpResponse()
