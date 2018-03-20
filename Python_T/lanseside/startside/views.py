from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from startside.models import Lanse, LED
from django.views.decorators import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from Blinky import on_off

# Create your views here.

@login_required
@ensure_csrf_cookie
def info(request):
    if request.method == 'GET':
        lanse = Lanse.objects.get(lanse_nr = 1)
        lanse = vars(lanse)
        del lanse['_state']
        return JsonResponse(lanse)
    if request.method == 'POST':
        lanse = Lanse.objects.get(lanse_nr = 1)
        lanse = vars(lanse)
        del lanse['_state']
        return JsonResponse(lanse)

@ensure_csrf_cookie
def startside(request):
    return(render(request, 'startside/startside.html'))

@ensure_csrf_cookie
def test(request):
    if request.method == 'GET':
        led = LED.objects.all()[0]
        state = led.stat
        args = {
            'state': state}
        return(render(request, 'test/test.html',args))
    elif request.method == 'POST':
        if hasattr(request.POST,'id'):
            id = request.POST['id']
            led = LED.objects.get(id=1) 
            if hasattr(request.POST,'state'):
                led.stat = request.POST['state']
                led.save()
                on_off(led.stat)
            del led['_state']
            return JsonResponse()
    else:
        return HttpResponse('')

@ensure_csrf_cookie
def lanser(request):
    if request.method == 'GET':
        return(render(request, 'startside/lanser.html'))
    elif request.method == 'POST':
        x = int(request.POST['lanse'])
        lanse = Lanse.objects.get(lanse_nr = x)
        lanse = vars(lanse)
        del lanse['_state']
        return JsonResponse(lanse)

@ensure_csrf_cookie
def valgtlanse(request):
    if request.method == 'GET':
        return JsonResponse({'info': 'dette var en get'})
    if request.method == 'POST':
        try:
            data = request.POST['test']
            print(data)
            lanse_nr = int(data[(data.find('Lanse'))+5:])
            print(lanse_nr)
            lanse = Lanse.objects.all().order_by('lanse_nr')[lanse_nr-1]
            ant_steg = lanse.ant_steg
        except:
            data = 'ingen lanse'
            ant_steg = 0
        finally:
            args = {'data': data,
                    'ant_steg': ant_steg
                    }
            #return JsonResponse(args)
            return(render(request, 'lansestyring/lansestyring.html', args))
    else:
        return HttpResponse('')