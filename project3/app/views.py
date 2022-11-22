from django.shortcuts import render

# Create your views here.
def firstPage(request):
    return render(request,'firstPage.html')