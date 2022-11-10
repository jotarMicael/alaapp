from tokenize import PseudoExtras
from django.shortcuts import redirect, render
from ludoscienceapp.models.user import User
from ludoscienceapp.models.check_in import CheckIn
from ludoscienceapp.models.proyect import Proyect
from ludoscienceapp.utils.System import System
from django.contrib import messages



def checkin(request):
    if System.is_logged(request):
        if System.is_player(request):
            return render (request,'ludoscienceapp/checkin/create_checkin.html',{'nav':'block','create_checkin':System.get_navbar_color,'proyects':User.objects.get(id__exact=request.session['id']).proyects.all()})      
        redirect('home')
    return redirect('index')  

def process_checkin(request):
    if System.is_logged(request):
        if System.is_player(request):
            if not request.POST['datetime'] or not request.POST['lat'] or not request.POST['lon'] or not request.POST['proyect']:
                  messages.error(request,'Debe ingresar todos los campos')
            else:  
                checkin_=CheckIn(user=(User.objects.get(id__exact=request.session['id'])),proyect=(Proyect.objects.get(id__exact=request.POST['proyect'])),latitude=request.POST['lat'],longitude=request.POST['lon'],datetime=request.POST['datetime'][:-3])
                checkin_.save()                  
                proyect = Proyect.objects.get(id__exact=request.POST['proyect'])
                proyect.add_checkin(checkin_,request.session['id'])

                messages.success(request,'CheckIn realizado correctamente')
            return checkin(request) 
        redirect('home')
    return redirect('index')  
