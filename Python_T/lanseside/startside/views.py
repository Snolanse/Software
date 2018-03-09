from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def startside(request):
    return(render(request, 'startside/startside.html'))

def lanser(request):
    return(render(request, 'startside/lanser.html'))

def valgtlanse(request):
    if request.method == 'GET':
        return JsonResponse({'info': 'fuck get'})
    if request.method == 'POST':
        data = request.POST['test']
        args = {'data': data}
        #return JsonResponse(args)
        return(render(request, 'lansestyring/lansestyring.html', args))
    else:
        return HttpResponse('')