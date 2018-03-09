from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def startside(request):
    return(render(request, 'startside/startside.html'))

def lanser(request):
    return(render(request, 'startside/lanser.html'))

def valgtlanse(request):
    if request.method == 'GET':
        return(render(request, 'lansestyring/lansestyring.html'))
    if request.method == 'POST':
        data = request.POST['test']
        args = {'data': data}
        return(render(request, 'lansestyring/lansestyring.html', args))
    else:
        return HttpResponse('')