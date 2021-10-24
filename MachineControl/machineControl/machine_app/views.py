from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    my_dict = {'insert_me' : '''I'm index'''}
    return render(request, 'index.html', context = my_dict)

def addUser(request):
    addu_dict = {'insert_me' : '''Add user'''}
    return render(request, 'index.html', context = addu_dict)
    # return HttpResponse('Hello add user')