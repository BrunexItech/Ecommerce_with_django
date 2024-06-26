from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1 style='color: blue;'>Bruno Sharif is my name!.Am here to stay buddies.</h1>")