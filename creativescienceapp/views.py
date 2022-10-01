from django.shortcuts import render
from django.conf import settings
from creativescienceapp.models import User
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'creativescienceapp/index.html')

def login(request):   
    if not request.POST['email'] or not request.POST['password']:
        return render(request,'creativescienceapp/index.html')    
    try:

        user=User.objects.get(email=request.POST['email'],password=request.POST['password'])
        #user=User.objects.get(username=request.POST['email'],password=request.POST['password'])
    except:
        return render(request,'creativescienceapp/index.html')   
    request.session['username'] = user.complete_name  
    request.session['profile_image'] = user.profile_image.url 
    
    if not user.verified:       
        f_send_mail(user)
        user.verified=True
        user.save()
        return verificate(request,user)
    return render(request,'creativescienceapp/home.html',{'request':request})

def verificate(request,user):
    return render(request, 'creativescienceapp/verificate.html',{ "user":user})

def  f_send_mail(user):
    subject="Bienvenido/a a CienciaCRE"
    message="Su código es: 1234"
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[user.email]
    send_mail(subject,message,email_from,recipient_list)