from django.shortcuts import render

# Create your views here.
def harry(request):
    return render(request,'harry.html')
def  moon(request):
    return render(request,'moon.html')
