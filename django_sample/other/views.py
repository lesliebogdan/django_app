from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def simple_view(request):
    return HttpResponse("<h1>HELLO bitchlet! This is a new web page</h1> <img src='vb.jpg'>>")
