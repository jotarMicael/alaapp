from django.shortcuts import redirect, render
from creativescienceapp.models import User
from creativescienceapp.utils.System import System
from django.contrib import messages
# Create your views here.
def index(request):
    if System.is_logged(request):
        return redirect('home')
    
    return render(request, 'creativescienceapp/index.html')

def home(request):
    if System.is_logged(request):
        return render(request, 'creativescienceapp/home.html')
    try:
        return login(request)    
    except:   
        
        return redirect('index')
    
    
def login(request):     
    
    if not request.POST['email'] or not request.POST['password']:
        return logout(request)
    try:   
        user=User.objects.get(email=request.POST['email'],password=request.POST['password'])
        #user=User.objects.get(username=request.POST['email'],password=request.POST['password'])
    except:
        messages.error(request,'Usuario/Email o contraseña incorrectos')
        return render(request,'index')
    System.set_session(request,user)    
    return verificate(request,user)

def verificate(request,user=False):
    if System.is_logged(request):
        try:
            if not user.verified:       
                System.f_send_mail(user)
                user.verified=True
                user.save()
                return render(request, 'creativescienceapp/verificate.html',{ "user":user})
            return redirect('home')
        except:
            pass
    return redirect('index')   

def logout(request):
        System.logout(request)
        return redirect('index')
    
