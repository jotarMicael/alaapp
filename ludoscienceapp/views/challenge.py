
from django.shortcuts import redirect, render
from ludoscienceapp.models.user import  User 
from ludoscienceapp.models.proyect import Proyect
from ludoscienceapp.models.proyect_area import ProyectArea
from ludoscienceapp.models.time_restriction import TimeRestriction
from ludoscienceapp.views import game_elements
from ludoscienceapp.models.challenge import Challenge
from ludoscienceapp.utils.System import System
from django.contrib import messages



def challenge(request):
    if System.is_logged(request):
          if System.is_admin(request):
                       
              return render(request, 'ludoscienceapp/game_elements/create_challenge.html',{'nav':'block','create_challenge':System.get_navbar_color,'proyects':Proyect.objects.all()})

def process_challenge(request):
    if System.is_logged(request):
          if System.is_admin(request):
              if not request.POST['name'] or not request.POST['area'] or not request.POST['proyect'] or not request.POST['time_restriction'] or not request.POST['goal']:
                  messages.error(request,'Debe ingresar todos los campos')
                  return challenge(request)               
              elif Challenge.objects.filter(name__iexact=request.POST['name'],proyect=Proyect.objects.get(id__exact=request.POST['proyect'])).exists():
                  messages.error(request,'Ya hay un desafío con ese nombre')
                  return challenge(request)    
              else: 
                challenge_=Challenge(name=request.POST['name'],area=ProyectArea.objects.get(id__exact=request.POST['area']),time_restriction=TimeRestriction.objects.get(id__exact=request.POST['time_restriction']),goal=request.POST['goal'],owner=User.objects.get(id__exact=request.session['id']),proyect=Proyect.objects.get(id__exact=request.POST['proyect']))
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
            user.add_challengue_active(challenge)
            messages.success(request,'Desafío %s  asignado con éxito'  % (challenge.get_name()))
            return game_elements.view_game_elements(request,challenge.get_id_proyect())
            
