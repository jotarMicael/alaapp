from email import message
from tokenize import PseudoExtras
from django.shortcuts import redirect, render
from creativescienceapp.models import Proyect, User, Role
from creativescienceapp.utils.System import System
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def create_proyect(request):
     if System.is_logged(request):
          if System.is_admin(request):
            return render (request,'creativescienceapp/create_proyect.html',{'nav':'block','create_proyect':System.get_navbar_color, 'admins':User.objects.filter(role_id__exact=Role.objects.get(name='ADMIN'))})      
          redirect('home')
     return redirect('index')  

def register_proyect(request):    
     if System.is_logged(request):
          if System.is_admin(request):        
            if not len(request.POST.getlist('select[]')) or not request.POST['name']:
               messages.error(request,'Debe ingresar todos los campos')
               return redirect('create_proyect') 
            proyect = Proyect(name=request.POST['name'])
            proyect.save()
            for admin_id in request.POST.getlist('select[]'):
                 ad=User.objects.get(id__exact=admin_id)
                 proyect.admins.add(ad)
            print(proyect)
            messages.success(request,'¡Proyecto creado con éxito¡')
            return redirect('create_proyect') 
     return redirect('index')  