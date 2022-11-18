
from django.shortcuts import redirect, render
from ludoscienceapp.models.user import  User 
from ludoscienceapp.models.project import Project

from ludoscienceapp.models.project_subarea import ProjectSubArea
from ludoscienceapp.models.time_restriction import TimeRestriction
from ludoscienceapp.views import game_elements
from ludoscienceapp.utils.System import System
from ludoscienceapp.models.badge import Badge
from ludoscienceapp.models.progress import Progress
from django.contrib import messages
from ludoscienceapp.forms import BadgeForm





def badge(request):
    if System.is_logged(request):
          if System.is_admin(request):
              return render(request, 'ludoscienceapp/game_elements/create_badge.html',{'nav':'block','create_badge':System.get_navbar_color,'badges':Badge.objects.all(),'projects':Project.objects.all()})


def process_badge(request):
    if System.is_logged(request):
          if System.is_admin(request):
              if not request.POST['name'] or not request.POST['area'] or not request.POST['project'] or not request.POST['time_restriction'] or not request.POST['goal']:
                  messages.error(request,'Debe ingresar todos los campos') 
                  return badge(request)               
              elif Badge.objects.filter(name__iexact=request.POST['name'],project=Project.objects.get(id__exact=request.POST['project'])).exists():
                  messages.error(request,'Ya hay una insignia con ese nombre') 
                  return badge(request)   
              badge_= Badge(name=request.POST['name'],area=ProjectSubArea.objects.get(id__exact=request.POST['area']),time_restriction=TimeRestriction.objects.get(id__exact=request.POST['time_restriction']),goal=request.POST['goal'],owner=User.objects.get(id__exact=request.session['id']),project=Project.objects.get(id__exact=request.POST['project']))                
              badge_.add_parent(int(request.POST['select']))    
              badge_.save()            
              form = BadgeForm(data=request.POST, files=request.FILES, instance=badge_)
              form.procces(badge_.get_path_image())
              messages.success(request,'Se ha creado correctamente')
              return badge(request)   
          return redirect('home')  
    return redirect('index') 

def asign_badge(request):
    if System.is_logged(request):
          if System.is_player(request):

            badge= Badge.objects.get(id=request.POST['badge_id'])
            user = User.objects.get(id=request.session['id'])
            user.add_gamelement_active(badge)
            bp = Progress(user=user,game_element=badge)
            bp.save()
            messages.success(request,'Insignia %s  asignado con éxito'  % (badge.get_name()))
            return game_elements.view_game_elements(request,badge.get_id_project())

