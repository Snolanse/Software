from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from startside.models import Lanse

# Create your views here.

def startside(request):
    return(render(request, 'startside/startside.html'))

def lanser(request):
    return(render(request, 'startside/lanser.html'))

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