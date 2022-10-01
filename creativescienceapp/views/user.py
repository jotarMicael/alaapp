from django.shortcuts import render
from creativescienceapp.models import User
from creativescienceapp.utils.System import System

# Create your views here.
def index(request):
    if (System.is_logged(request)):
        return render(request,'creativescienceapp/home.html')
    return render(request,'creativescienceapp/index.html')

def login(request):     
    if not request.POST['email'] or not request.POST['password']:
        return render(request,'creativescienceapp/index.html')    
    try:
        user=User.objects.get(email=request.POST['email'],password=request.POST['password'])
        #user=User.objects.get(username=request.POST['email'],password=request.POST['password'])
    except:
        return render(request,'creativescienceapp/index.html')   
    System.set_session(request,user)
    if not user.verified:       
        System.f_send_mail(user)
        user.verified=True
        user.save()
        return verificate(request,user)
    return render(request,'creativescienceapp/home.html',{'request':request})

def verificate(request,user):
    return render(request, 'creativescienceapp/verificate.html',{ "user":user})




    