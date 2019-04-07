from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    qqq = "asdasd"
    template = loader.get_template('bm/index.html')
    context = {
        'latest_question_list': qqq,
    }
    return HttpResponse(template.render(context, request))