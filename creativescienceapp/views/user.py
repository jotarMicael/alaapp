
from tokenize import PseudoExtras
from django.shortcuts import redirect, render
from creativescienceapp.models import User,Role,Token, Proyect
from creativescienceapp.utils.System import System
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from werkzeug.security import generate_password_hash,check_password_hash


# Create your views here.

def index(request):
    if System.is_logged(request):
        return redirect('home')   
    return render(request, 'creativescienceapp/index.html')

def register(request):
    if System.is_logged(request):
        return redirect('home')   
    return render(request, 'creativescienceapp/register.html')

def home(request):
    if System.is_logged(request):
        proyects=Proyect.objects.filter(admins__id=request.session['id'])
        return render(request, 'creativescienceapp/home.html',{'proyects':proyects})    
    return redirect('index')
    
    
def login(request):     
    
    if not request.POST['email'] or not request.POST['password']:
        messages.error(request,'Debe ingresar todos los campos')
        return redirect('index')    
    try:  
        if '@' in request.POST['email']:
            user=User.objects.get( email__iexact=request.POST['email'])
        else:
            user=User.objects.get( username__iexact=request.POST['email'])    
        if not check_password_hash(user.password,request.POST['password']):
           raise ObjectDoesNotExist 
    except ObjectDoesNotExist:

        messages.error(request,'Usuario/Email o contraseña incorrectos')
        return redirect('index')
    System.set_session(request,user)        
    return user_verificate(request,False,user)

def user_verificate(request,ok=False,user=False):  
    try:
        if not user.verified:  
            if ok:  
                System.f_send_mail(user)               
            return redirect('verificate')
        return redirect('home')
    except:
        return redirect('index')   
    

def logout(request):
        System.logout(request)       
        return redirect('index')
    
def register_user(request):
    if System.is_logged(request):    
        return redirect('home')       
    if User.objects.filter(email__exact=request.POST['email']).exists() or  User.objects.filter(username__exact=request.POST['username']).exists():
        messages.error(request,'Nombre de usuario/email ya utilizado')
        System.logout
        return redirect('register')
    if not request.POST['email'] or not request.POST['username'] or not request.POST['password'] or not request.POST['repeat_password'] or not request.POST['name'] or (request.POST['password'] != request.POST['repeat_password']):
        if (request.POST['password'] != request.POST['repeat_password']):
            messages.error(request,'Las contraseñas no coinciden')
        else:
            messages.error(request,'Todos los campos deben estar completos')
        return redirect('register')
        
    user=User(email=request.POST['email'],username=request.POST['username'],complete_name=request.POST['name'],role_id=Role.objects.get(name='PLAYER'),password=generate_password_hash(request.POST['password'], 'sha256', 10))
    user.save()
    System.set_session(request,user)  
    return user_verificate(request,True,user)

def verificate(request):
    return render (request,'creativescienceapp/verificate/verificate.html')

def activate_account(request):       
    user_id=System.decode_token(request.GET.get('token')[:15],request.GET.get('token')[15:len(request.GET.get('token'))])
    if user_id:
        user=User.objects.get(id=user_id)
        user.verified=True
        user.save()
        logout(request)
        request.session['av']=True 
        return redirect('active_account')
        

def active_account(request):
    try:
        del request.session['av']
        return render (request,'creativescienceapp/verificate/active_account.html')   
    except KeyError:
        return redirect('index')  

