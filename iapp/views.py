from django.shortcuts import render

# Create your views here.

def first(request):
    return render(request,'first.html')

def addleads(request):
    return render(request,'table1.html')
