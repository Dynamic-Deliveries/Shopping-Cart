from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the shopping cart index.")

def restaurant_archive(request):
    html = #html formatting goes here
    return HttpResopnse(html)

def restaurant(request, rest_id):
    html = #html formatting goes here
    return HttpResopnse(html)
def menu(request):
    html = #html formatting goes here
    return HttpResopnse(html)


