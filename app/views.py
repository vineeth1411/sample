from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first(request):
    return HttpResponse('This is my first FunctionBasedView')


def second(request):
    return HttpResponse('This is my second FunctionBasedView')
