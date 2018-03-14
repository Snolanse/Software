from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from startside.models import Lanse
from django.views.decorators import csrf
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

@ensure_csrf_cookie
def info(request):
    if request.method == 'GET':
        lanse = Lanse.objects.get(lanse_nr = 1)
        lanse = vars(lanse)
        del lanse['_state']
        return JsonResponse(lanse)

@ensure_csrf_cookie
def startside(request):
    return(render(request, 'startside/startside.html'))

@ensure_csrf_cookie
def lanser(request):
    if request.method == 'GET':
        return(render(request, 'startside/lanser.html'))
    elif request.method == 'POST':
        lanse = Lanse.objects.get(lanse_nr = 1)
        return JsonResponse()

@ensure_csrf_cookie
def valgtlanse(request):
    if request.method == 'GET':
        return JsonResponse({'info': 'dette var en get'})
    if request.method == 'POST':
        data = request.POST['test']
        print(data)
        lanse_nr = int(data[(data.find('Lanse'))+5:])
        print(lanse_nr)
        lanse = Lanse.objects.all().order_by('lanse_nr')[lanse_nr-1]
        ant_steg = lanse.ant_steg
        args = {'data': data,
                'ant_steg': ant_steg
                }
        #return JsonResponse(args)
        return(render(request, 'lansestyring/lansestyring.html', args))
    else:
        return HttpResponse('')