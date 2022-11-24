
from django.shortcuts import redirect, render
import json
from alaapp.models.project import Project
from alaapp.models.user import User
from alaapp.models.role import Role
from alaapp.models.project_area import ProjectArea
from alaapp.models.project_subarea import ProjectSubArea
from alaapp.models.time_restriction import TimeRestriction
from alaapp.models.challenge import Challenge
from alaapp.models.game_element import GameElement
from alaapp.models.badge import Badge
from alaapp.utils.System import System
from django.contrib import messages
from alaapp.forms import ProjectForm
import geopandas as gpd


def create_project(request):
     if System.is_logged(request):
          if System.is_root(request):
            return render (request,'alaapp/projects/create_project.html',{'nav':'block','create_project':System.get_navbar_color, 'admins':User.objects.filter(role_id__exact=Role.objects.get(name='ADMIN'))})      
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
            project.add_admins(request.POST.getlist('select[]'))
            messages.success(request,'¡Proyecto creado con éxito¡')
            return redirect('create_project') 
     return redirect('index')  

def modify_project(request):
    if System.is_logged(request):
          if System.is_admin(request):
               return render (request,'alaapp/projects/modify_project.html',{'nav':'block','create_admin':System.get_navbar_color, 'project':Project.objects.get(id__exact=request.POST.get('id')),'areas':ProjectArea.objects.all(),'time_restrictions':TimeRestriction.objects.all()})      
          redirect('home')
    return redirect('index') 


def edit_project(request):

     if System.is_logged(request):
          if System.is_admin(request): 
                              
                if not request.POST.get('name') or not request.POST.get('description') or not request.FILES.get('image') or not request.FILES.get('area') or len(request.POST.getlist('time_restriction[]'))==0 :
                     messages.error(request,'Debe ingresar todos los campos')
                     return modify_project(request)

                project=Project.objects.get(id__exact=request.POST['id'])
                project.modify(request.POST['name'],request.POST['description'],request.POST.get('checkbox'))             
                               
                df = gpd.read_file(request.FILES.get('area'), driver='GeoJSON')   
                area=json.loads(df.to_json())
                p_area= ProjectArea(name=area['type'])
                p_area.save()
                p_area.add_subareas(area['features'])
                project.add_area(p_area)     
                project.add_time_restrictions(request.POST.getlist('time_restriction[]'))
                project.save()           
                form = ProjectForm(data=request.POST, files=request.FILES, instance=project)
                form.procces(project.get_image_path())
                return redirect('home') 

def game_elements_project(request,ok=False):
     if System.is_logged(request):
          if System.is_admin(request): 
               if not ok:
                    project_=Project.objects.get(id__exact=request.POST['id'])
               else:
                    project_=Project.objects.get(id__exact=ok)                    
          
               return render (request,'alaapp/game_elements/game_elements_project.html',{'nav':'block','game_elements_project':System.get_navbar_color, 'project_name':project_.get_name(),'challenges':Challenge.objects.filter(project=project_),'badges': Badge.objects.filter(project=project_)})      

def see_all_projects(request):
     if System.is_logged(request):
          if System.is_player(request):         
               return render (request,'alaapp/projects/see_all_projects.html',{'nav':'block','see_all_projects':System.get_navbar_color, 'projects':Project.objects.filter(avaliable=True).exclude(user__id=request.session['id']) } )      


def asign_project(request):
     if System.is_logged(request):
          if System.is_player(request): 
               project= Project.objects.get(id=request.POST['project_id'])
               User.objects.get(id=request.session['id']).add_project(project)
               messages.success(request,'¡Proyecto %s añadido exitosamente!' % (project.get_name()))  
               return see_all_projects(request) 