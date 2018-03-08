from django.shortcuts import render

# Create your views here.

def startside(request):
    return(render(request, 'startside/startside.html'))

def lanser(request):
    return(render(request, 'lanser/lanser.html'))