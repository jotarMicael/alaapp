
from django.shortcuts import redirect, render
import json
from ludoscienceapp.models.project import Project
from ludoscienceapp.models.user import User
from ludoscienceapp.models.role import Role
from ludoscienceapp.models.project_area import ProjectArea
from ludoscienceapp.models.project_subarea import ProjectSubArea
from ludoscienceapp.models.time_restriction import TimeRestriction
from ludoscienceapp.models.challenge import Challenge
from ludoscienceapp.models.game_element import GameElement
from ludoscienceapp.models.badge import Badge
from ludoscienceapp.utils.System import System
from django.contrib import messages
from ludoscienceapp.forms import ProjectForm
import geopandas as gpd
import os

def create_project(request):
     if System.is_logged(request):
          if System.is_root(request):
            return render (request,'ludoscienceapp/projects/create_project.html',{'nav':'block','create_project':System.get_navbar_color, 'admins':User.objects.filter(role_id__exact=Role.objects.get(name='ADMIN'))})      
          redirect('home')
     return redirect('index')  

def register_project(request):    
     if System.is_logged(request):
          if System.is_root(request):        
            if not len(request.POST.getlist('select[]')) or not request.POST['name']:
               messages.error(request,'Debe ingresar todos los campos')
               return redirect('create_project') 
            project = Project(name=request.POST['name'])
            project.save()
            for admin_id in request.POST.getlist('select[]'):
                 ad=User.objects.get(id__exact=admin_id)
                 project.admins.add(ad)
            messages.success(request,'¡Proyecto creado con éxito¡')
            return redirect('create_project') 
     return redirect('index')  

def modify_project(request):
    if System.is_logged(request):
          if System.is_admin(request):
               return render (request,'ludoscienceapp/projects/modify_project.html',{'nav':'block','create_admin':System.get_navbar_color, 'project':Project.objects.get(id__exact=request.POST.get('id')),'areas':ProjectArea.objects.all(),'time_restrictions':TimeRestriction.objects.all()})      
          redirect('home')
    return redirect('index') 


def edit_project(request):

     if System.is_logged(request):
          if System.is_admin(request): 
                              
                if not request.POST.get('name') or not request.POST.get('description') or not request.FILES.get('image') or not request.FILES.get('area') or len(request.POST.getlist('time_restriction[]'))==0:
                     messages.error(request,'Debe ingresar todos los campos')
                     return modify_project(request)

                project=Project.objects.get(id__exact=request.POST['id'])
                project.modify(request.POST['name'],request.POST['description'],request.POST.get('checkbox'))             
                               
                df = gpd.read_file(request.FILES.get('area'), driver='GeoJSON')   
                area=json.loads(df.to_json())
                p_area= ProjectArea(name='Nombre-Fantasia',type=area['type'])
                p_area.save()
                project.add_area(p_area)        
                for subarea in area['features']:
                    p_subarea=ProjectSubArea(area=p_area,sub_area=json.dumps(subarea))
                    p_subarea.save()
                for time_restriction_id in request.POST.getlist('time_restriction[]'):
                    project.add_time_restriction(TimeRestriction.objects.get(id__exact=time_restriction_id))

                project.save()    
               
                form = ProjectForm(data=request.POST, files=request.FILES, instance=project)
                if form.is_valid():
                    
                    if os.path.exists(project.image.path):
                         os.remove(project.image.path)
                    form.save()
                return redirect('home') 

def game_elements_project(request,ok=False):
     if System.is_logged(request):
          if System.is_admin(request): 
               if not ok:
                    project_=Project.objects.get(id__exact=request.POST['id'])
               else:
                    project_=Project.objects.get(id__exact=ok)                    
          
               return render (request,'ludoscienceapp/game_elements/game_elements_project.html',{'nav':'block','game_elements_project':System.get_navbar_color, 'project_name':project_.get_name(),'challenges':Challenge.objects.filter(project=project_),'badges': Badge.objects.filter(project=project_)})      

