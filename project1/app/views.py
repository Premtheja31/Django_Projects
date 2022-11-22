from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("<marquee>first view function</marquee>")

def propose(request):
    return HttpResponse("<h1>yes i love u too</h1>")

def rejection(request):
    return HttpResponse("<marquee>No i am really sorry</marquee>")