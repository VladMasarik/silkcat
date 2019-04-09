from django.shortcuts import render
from django.http import HttpResponse
from blackmarket.models import Cat
from django import forms
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        print("method>>>",request.method)
        form = ImaageForm(request.POST)
        form2 = OneForm(request.POST, request.FILES)
        print("Errors:", form.errors.as_data())
        print("form>>>",form)
        print("valid>>", form.is_valid())
        if form.is_valid():
            print("<<<<<<", form.cleaned_data, ">>>>>>>>>")
        print("Errors:", form2.errors.as_data())
        print("form>>>",form2)
        print("valid>>", form2.is_valid())
        if form2.is_valid():
            print("<<<<<<", form2.cleaned_data, ">>>>>>>>>")
    form = ImaageForm()
    imgform = OneForm()
    context = {
        "form": form,
        "imageinput": imgform
    }
    return HttpResponse(render(request, "bm/upload.html", context))


def delete(request, id):
    Cat.objects.get(id=id).delete()
    return HttpResponse()

class ImaageForm(forms.Form):
    name = forms.CharField(label='Cats name', max_length=100)
    size = forms.CharField(label='Cats size', max_length=100)
    color = forms.CharField(label='Cats color', max_length=100)

class OneForm(forms.Form):
    img = forms.ImageField()