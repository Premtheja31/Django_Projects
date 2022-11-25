from django.shortcuts import render

# Create your views here.
def a2_first(request):
    return render(request,'a2_first.html',{'a':10,'b':20,'c':30})
def a2_second(request):
    return render(request,'a2_second.html',{'name':'hai this is my first for loop'})