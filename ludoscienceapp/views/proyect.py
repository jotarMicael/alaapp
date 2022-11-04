
from django.shortcuts import redirect, render
from ludoscienceapp.models.proyect import Proyect
from ludoscienceapp.models.user import User
from ludoscienceapp.models.role import Role
from ludoscienceapp.models.proyect_area import ProyectArea
from ludoscienceapp.models.time_restriction import TimeRestriction
from ludoscienceapp.utils.System import System
from django.contrib import messages
from ludoscienceapp.forms import ProyectForm

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
               return render (request,'ludoscienceapp/proyects/modify_proyect.html',{'nav':'block','create_admin':System.get_navbar_color, 'proyect':Proyect.objects.get(id__exact=request.POST.get('id')),'areas':ProyectArea.objects.all(),'time_restrictions':TimeRestriction.objects.all()})      
          redirect('home')
    return redirect('index') 


def edit_proyect(request):

     if System.is_logged(request):
          if System.is_admin(request):      
                if not request.POST.get('name') or not request.POST.get('description') or not request.FILES.get('image') or  len(request.POST.getlist('area[]'))==0 or not not len(request.POST.getlist('time_restriction[]'))==0:
                     messages.error(request,'Debe ingresar todos los campos')
                     return modify_proyect(request)
                proyect=Proyect.objects.get(id__exact=request.POST['id'])
                proyect.name=request.POST['name']
                proyect.description=request.POST['description']              
                if request.POST.get('checkbox') == 'on':
                    proyect.avaliable=1
                else:
                    proyect.avaliable=0
                for area_id in request.POST.getlist('area[]'):
                    area=ProyectArea.objects.get(id__exact=area_id)
                    proyect.areas.add(area)
                for time_restriction_id in request.POST.getlist('time_restriction[]'):
                    time_restriction=TimeRestriction.objects.get(id__exact=time_restriction_id)
                    proyect.time_restriction.add(time_restriction)
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
                     


