from django.shortcuts import render, redirect
from django.http import HttpResponse
from blackmarket.models import Cat
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

import boto3



def index(request):


    s = boto3.resource('s3')
    db = boto3.resource('dynamodb')
    table = db.Table('kittyfolder')
    cats = []
    for i in table.scan()["Items"]:
        kit = Cat()
        kit.name = i["name"]
        kit.size = i["size"]
        kit.color = i["color"]
        kit.image = i["url"]
        print(kit.image.name)
        s.Bucket("kittyfolder").download_file(str(kit.image), "blackmarket/static/blackmarket/{}".format(str(kit.image.name)))
        kit.id = i["iddd"]
        cats.append(kit)




    context = {
        "cat_list": cats,
    }

    return HttpResponse(render(request, "bm/index.html", context))


def detail(request, id):

    s = boto3.resource('s3')
    db = boto3.resource('dynamodb')
    table = db.Table('kittyfolder')
    
    try:
        int(id)
    except ValueError:
        return redirect("/")

    cat = None

    try:

        print(id)
        response = table.get_item(Key={'iddd': int(id)})
        item = response['Item']

        print(item)
        
        cat = Cat()

        cat.name = item["name"]
        cat.size = item["size"]
        cat.color = item["color"]
        cat.image = item["url"]
        cat.id = item['iddd']

        # "blackmarket/static/blackmarket/{}".format(cat.image.url)


        s.Bucket("kittyfolder").download_file(cat.image.url, "blackmarket/static/blackmarket/{}".format(cat.image.url))
        # cat = Cat.objects.get(id=id)
        # print(cat.image)

        print(cat)
    except ObjectDoesNotExist:
        return redirect("/")

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
    #cat = Cat.objects.get(id=id)
    cat = None
    s = boto3.resource('s3')
    db = boto3.resource('dynamodb')
    table = db.Table('kittyfolder')

    if request.method == 'POST':
        form = TextInputForm(request.POST)
        form2 = EditImageInputForm(request.POST, request.FILES)
        if form.is_valid():


            table.update_item(
                Key={
                    'iddd': int(id)
                },
                UpdateExpression='SET color = :val2',
                ExpressionAttributeValues={
                    ":val2": form.cleaned_data["color"]
                }
            )

            desc = form.cleaned_data["name"]
            
            table.update_item(
                Key={
                    'iddd': int(id)
                },
                UpdateExpression='SET #qqq = :val1',
                ExpressionAttributeValues={
                    ':val1': desc
                },
                ExpressionAttributeNames={
                    "#qqq": "name"
                }
            )

            table.update_item(
                Key={
                    'iddd': int(id)
                },
                UpdateExpression='SET size = :val3',
                ExpressionAttributeValues={
                    ":val3": form.cleaned_data["size"]
                }
            )








            cat = Cat()


            cat.name = form.cleaned_data["name"]
            cat.size = form.cleaned_data["size"]
            cat.color = form.cleaned_data["color"]
            cat.save()
        
        if  form2.is_valid() and form2.cleaned_data["img"] != None:
            cat.image = form2.cleaned_data["img"]
            print("cat.image.name",cat.image.name)

            hhh = cat.image.name

            table.update_item(
                Key={
                    'iddd': int(id)
                },
                UpdateExpression='SET #ccc = :val4',
                ExpressionAttributeValues={
                    ":val4": cat.image.name
                },
                ExpressionAttributeNames={
                    "#ccc": "url"
                }
            )
            cat.save()
            print("cat.image.name",hhh)
            s.meta.client.upload_file("blackmarket/static/blackmarket/{}".format(hhh), "kittyfolder", hhh)
            

    imgform = EditImageInputForm()


    print(id)
    response = table.get_item(Key={'iddd': int(id)})
    item = response['Item']

    print(item)
    
    cat = Cat()

    cat.name = item["name"]
    cat.size = item["size"]
    cat.color = item["color"]
    cat.image = item["url"]
    cat.id = item['iddd']

    # "blackmarket/static/blackmarket/{}".format(cat.image.url)


    s.Bucket("kittyfolder").download_file(cat.image.url, "blackmarket/{}".format(cat.image.url))


    # response = table.get_item(Key={'iddd': int(id)})
    # item = response['Item']

    # print(item)
    # s.Bucket("kittyfolder").download_file(item["url"], "blackmarket/static/blackmarket/{}".format(item["url"]))



    # tmp = cat
    # cat = Cat()

    # cat.name = item["name"]
    # cat.size = item["size"]
    # cat.color = item["color"]
    # cat.image = item["url"]
    # cat.id = item['iddd']

    # "blackmarket/static/blackmarket/{}".format(cat.image.url)





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
            s = boto3.resource('s3')
            db = boto3.resource('dynamodb')
            table = db.Table('kittyfolder')
            # print(table.scan()["Items"])
            ids = []
            for i in table.scan()["Items"]:
                ids.append(i["iddd"])

            print(ids)

            num = 0
            while True:
                if num in ids:
                    num += 1
                    continue
                print(num)
                break
            image = form2.cleaned_data["img"]
            print("image name",image.name)
            table.put_item(
                Item={
                    "iddd" : num,
                    'name': form.cleaned_data["name"],
                    'size': form.cleaned_data["size"],
                    'color': form.cleaned_data["color"],
                    'url': image.name,
                }
            )



            cat = Cat()
            cat.name = form.cleaned_data["name"]
            cat.size = form.cleaned_data["size"]
            cat.color = form.cleaned_data["color"]
            cat.image = form2.cleaned_data["img"]
            cat.save()

            s.meta.client.upload_file("blackmarket/static/blackmarket/{}".format(image.name), "kittyfolder", image.name)

    form = TextInputForm()
    imgform = ImageInputForm()
    context = {
        "form": form,
        "imageinput": imgform
    }
    return HttpResponse(render(request, "bm/upload.html", context))


def delete(request, id):

    s = boto3.resource('s3')
    db = boto3.resource('dynamodb')
    table = db.Table('kittyfolder')
    table.delete_item(
        Key={
            'iddd': int(id)
        }
    )
    return redirect('/')

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