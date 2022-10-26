from email import message
from tokenize import PseudoExtras
from django.shortcuts import redirect, render
<<<<<<< HEAD:ludoscienceapp/views/proyect.py
from ludoscienceapp.models.proyect import Proyect
from ludoscienceapp.models.user import User
from ludoscienceapp.models.role import Role
from ludoscienceapp.utils.System import System
=======
from creativescienceapp.models.proyect import Proyect
from creativescienceapp.models.user import User
from creativescienceapp.models.role import Role
from creativescienceapp.utils.System import System
>>>>>>> fc50664f765aba41ae26cac3f94c5b094dfcf932:creativescienceapp/views/proyect.py
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from ludoscienceapp.forms import ProyectForm
from django.conf import settings
import os
def create_proyect(request):
     if System.is_logged(request):
          if System.is_root(request):
            return render (request,'ludoscienceapp/proyects/create_proyect.html',{'nav':'block','create_proyect':System.get_navbar_color, 'admins':User.objects.filter(role_id__exact=Role.objects.get(name='ADMIN'))})      
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
            messages.success(request,'¡Proyecto creado con éxito¡')
            return redirect('create_proyect') 
     return redirect('index')  

def modify_proyect(request):
    if System.is_logged(request):
          if System.is_admin(request):
               return render (request,'ludoscienceapp/proyects/modify_proyect.html',{'nav':'block','create_admin':System.get_navbar_color, 'proyect':Proyect.objects.get(id__exact=request.POST.get('id'))})      
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
                     


