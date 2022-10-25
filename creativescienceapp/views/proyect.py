from email import message
from tokenize import PseudoExtras
from django.shortcuts import redirect, render
from creativescienceapp.models import Proyect, User, Role
from creativescienceapp.utils.System import System
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from creativescienceapp.forms import ProyectForm
from django.conf import settings
import os
def create_proyect(request):
     if System.is_logged(request):
          if System.is_root(request):
            return render (request,'creativescienceapp/proyects/create_proyect.html',{'nav':'block','create_proyect':System.get_navbar_color, 'admins':User.objects.filter(role_id__exact=Role.objects.get(name='ADMIN'))})      
          redirect('home')
     return redirect('index')  

def register_proyect(request):    
     if System.is_logged(request):
          if System.is_root(request):        
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

def modify_proyect(request):
    if System.is_logged(request):
          if System.is_admin(request):
               return render (request,'creativescienceapp/proyects/modify_proyect.html',{'nav':'block','create_admin':System.get_navbar_color, 'proyect':Proyect.objects.get(id__exact=request.POST.get('id'))})      
          redirect('home')
    return redirect('index') 


def edit_proyect(request):

     if System.is_logged(request):
          if System.is_admin(request):      
                if not request.POST.get('name') or not request.POST.get('description') or not request.FILES.get('image'):
                     messages.error(request,'Debe ingresar todos los campos')
                     return modify_proyect(request)
                proyect=Proyect.objects.get(id__exact=request.POST['id'])
                proyect.name=request.POST['name']
                proyect.description=request.POST['description']              
                if request.POST.get('checkbox') == 'on':
                    proyect.avaliable=1
                else:
                    proyect.avaliable=0
                proyect.save()
                form = ProyectForm(data=request.POST, files=request.FILES, instance=proyect)
                if form.is_valid():
                     # deleting old uploaded image.
                    if os.path.exists(proyect.image.path):
                         os.remove(proyect.image.path)
                    form.save()
                    return redirect('home') 
                
               
                
                #messages.success(request,'¡Proyecto actualizado con éxito¡')
                #return redirect('modify_proyect',{'proyect':proyect}) 
                     


