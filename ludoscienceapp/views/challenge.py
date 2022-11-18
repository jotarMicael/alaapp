
from django.shortcuts import redirect, render
from ludoscienceapp.models.user import  User 
from ludoscienceapp.models.project import Project

from ludoscienceapp.models.project_area import ProjectArea
from ludoscienceapp.models.project_subarea import ProjectSubArea
from ludoscienceapp.models.time_restriction import TimeRestriction
from ludoscienceapp.views import game_elements
from ludoscienceapp.models.challenge import Challenge
from ludoscienceapp.models.game_element import GameElement
from ludoscienceapp.models.progress import Progress
from ludoscienceapp.utils.System import System
from django.contrib import messages



def challenge(request):
    if System.is_logged(request):
          if System.is_admin(request):
                       
              return render(request, 'ludoscienceapp/game_elements/create_challenge.html',{'nav':'block','create_challenge':System.get_navbar_color,'projects':Project.objects.all()})

def process_challenge(request):
    if System.is_logged(request):
          if System.is_admin(request):
              if not request.POST['name'] or not request.POST['area'] or not request.POST['project'] or not request.POST['time_restriction'] or not request.POST['goal']:
                  messages.error(request,'Debe ingresar todos los campos')
                  return challenge(request)               
              elif Challenge.objects.filter(name__iexact=request.POST['name'],project=Project.objects.get(id__exact=request.POST['project'])).exists():
                  messages.error(request,'Ya hay un desafío con ese nombre')
                  return challenge(request)    
              else: 
                challenge_=Challenge(name=request.POST['name'],area=ProjectSubArea.objects.get(id__exact=request.POST['area']),time_restriction=TimeRestriction.objects.get(id__exact=request.POST['time_restriction']),goal=request.POST['goal'],owner=User.objects.get(id__exact=request.session['id']),project=Project.objects.get(id__exact=request.POST['project']))
                challenge_.save()            
                messages.success(request,'Se ha creado correctamente')
              return challenge(request) 
          return redirect('home')  
    return redirect('index')  

def asign_challenge(request):
    if System.is_logged(request):
          if System.is_player(request):

            challenge= Challenge.objects.get(id=request.POST['challenge_id'])
            user = User.objects.get(id=request.session['id'])
            user.add_gamelement_active(challenge)
            cp = Progress(user=user, game_element=challenge)
            cp.save()
            messages.success(request,'Desafío %s  asignado con éxito'  % (challenge.get_name()))
            return game_elements.view_game_elements(request,challenge.get_id_project())
            
def modify_challenge(request):
    if System.is_logged(request):
          if System.is_admin(request):
              if not request.POST['name'] or not request.POST['area'] or  not request.POST['time_restriction'] or not request.POST['goal']:
                  messages.error(request,'Debe ingresar todos los campos')
                  return game_elements.modify(request,True)               
              elif Challenge.objects.filter(name__iexact=request.POST['name'],project=Project.objects.get(id__exact=request.POST['id_project'])).exclude(id__exact=request.POST['id']).exists():
                  messages.error(request,'Ya hay un desafío con ese nombre')
                  return game_elements.modify(request,True)       
              else: 
                challenge_=Challenge.objects.get(id__exact=request.POST['id'])
                challenge_.update(request.POST['name'],ProjectSubArea.objects.get(id__exact=request.POST['area']),TimeRestriction.objects.get(id__exact=request.POST['time_restriction']),request.POST['goal'])           
                messages.success(request,'Desafío modificado correctamente')
              return game_elements.modify(request,True)     
          return redirect('home')  
    return redirect('index')  
