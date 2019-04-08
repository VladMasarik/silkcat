from django.shortcuts import render
from django.http import HttpResponse
from blackmarket.models import Cat

"""
wizard
long
bongo
grumpy
https://i.imgur.com/AYTaKY9.jpg
https://7gigzxopz0uiqxo1-zippykid.netdna-ssl.com/wp-content/uploads/2015/07/cat.jpg
https://img.buzzfeed.com/buzzfeed-static/static/2018-10/5/12/asset/buzzfeed-prod-web-03/sub-buzz-29911-1538758090-1.jpg
https://www.tapatalk.com/groups/animaluntamed/imageproxy.php?url=http://i917.photobucket.com/albums/ad19/JinenFordragon/541252ef91e16735b792945a4c260111e43225a.jpg
https://cdn.themindcircle.com/wp-content/uploads/2017/08/funny-cat-fails-1.jpg
https://sadanduseless.b-cdn.net/wp-content/uploads/2018/08/burrito3.jpg
ninja
box
old school
"""

def index(request):

    cats = Cat.objects.all()
    context = {
        "cat_list": cats,
    }

    return HttpResponse(render(request, "bm/index.html", context))


def detail(request, id):

    cat = Cat.objects.get(id=id)

    context = {
        "name" : cat.name,
        "size" : cat.size,
        "color" : cat.color,
        "image" : cat.image_path,
        "id": cat.id
    }
    return HttpResponse(render(request, "bm/detail.html", context))


def edit(request, id):
    cat = Cat.objects.get(id=id)

    context = {
        "name" : cat.name,
        "size" : cat.size,
        "color" : cat.color,
        "image" : cat.image_path,
        "id": cat.id
    }
    return HttpResponse(render(request, "bm/edit.html", context))



def upload(request):
    Cat.objects.create(name="wizard", size="small", color="red", image_path="liquid.jpg")
    context = {}
    return HttpResponse(render(request, "bm/upload.html", context))


def delete(request, id):
    Cat.objects.get(id=id).delete()
    return HttpResponse()
