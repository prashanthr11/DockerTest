from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request, name):
    return HttpResponse('hello ' + name + '!!')

def index(request):
    return HttpResponse('home page')