from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h2>Funk plz, da gjør du meg glad</h2>")
    with open('C:/Users/marius/Pictures/Saved Pictures/kRhZs5d.png' ,"rb") as f:
        return HttpResponse( f.read(), content_type="image/png")

def index2(request):
    return HttpResponse("<h2>Dayman!</h2>")