from django.shortcuts import render
import datetime
#from PIL import Image

def home(request):
    numbers = [1,2,3,4,5]
    name = 'Per Gunnar Torvund'
    tid = datetime.datetime.now()

    args = {'myName': name,
           'numbers': numbers,
           'aar': tid.year,
           'maaned': tid.month,
           'dag': tid.day,
           'time': tid.hour,
           'minutt': tid.minute,
           'sekund': tid.second
           }

    return render(request, 'accounts/home.html', args)

def divtest(request):
    #img = Image.open('Dusj.png')
    #img.show()
    return(1)

def submit(request):
    info=request.POST['info']
    print(info)
    #img = Image.open('C:/Users/marius/Pictures/Saved Pictures/bk98GsW.jpg')
    #img.show()
    return (1)

