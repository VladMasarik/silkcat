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
        "image_url" : cat.image.url,
        "id": cat.id
    }
    return HttpResponse(render(request, "bm/detail.html", context))


@csrf_exempt
def edit(request, id):
    cat = Cat.objects.get(id=id)

    if request.method == 'POST':
        form = TextInputForm(request.POST)
        form2 = EditImageInputForm(request.POST, request.FILES)
        if form.is_valid():
            cat.name = form.cleaned_data["name"]
            cat.size = form.cleaned_data["size"]
            cat.color = form.cleaned_data["color"]
            cat.save()
        
        if  form2.is_valid() and form2.cleaned_data["img"] != None:
            cat.image = form2.cleaned_data["img"]
            cat.save()

    imgform = EditImageInputForm()
    name = Name(initial={"name": cat.name})
    size = Size(initial={"size": cat.size})
    color = Color(initial={"color": cat.color})
    context = {
        "imageinput": imgform,
        "cat": cat,
        "name": name,
        "size": size,
        "color": color
    }
    return HttpResponse(render(request, "bm/edit.html", context))


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        form2 = ImageInputForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            cat = Cat()
            cat.name = form.cleaned_data["name"]
            cat.size = form.cleaned_data["size"]
            cat.color = form.cleaned_data["color"]
            cat.image = form2.cleaned_data["img"]
            cat.save()
    form = TextInputForm()
    imgform = ImageInputForm()
    context = {
        "form": form,
        "imageinput": imgform
    }
    return HttpResponse(render(request, "bm/upload.html", context))


def delete(request, id):
    Cat.objects.get(id=id).delete()
    return HttpResponse()

class TextInputForm(forms.Form):
    name = forms.CharField(label='Cat name', max_length=100)
    size = forms.CharField(label='Cat size', max_length=100)
    color = forms.CharField(label='Cat color', max_length=100)

class ImageInputForm(forms.Form):
    img = forms.ImageField(label='Kitty image:')

class EditImageInputForm(forms.Form):
    img = forms.ImageField(required=False, label='Kitty image:')



class Color(forms.Form):
    color = forms.CharField(label='Cat color', max_length=100)

class Size(forms.Form):
    size = forms.CharField(label='Cat size', max_length=100)

class Name(forms.Form):
    name = forms.CharField(label='Cat name', max_length=100)