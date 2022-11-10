
from django.shortcuts import redirect, render
from ludoscienceapp.models.user import  User 
from ludoscienceapp.models.proyect import Proyect
from ludoscienceapp.models.proyect_area import ProyectArea
from ludoscienceapp.models.time_restriction import TimeRestriction
from ludoscienceapp.models.challenge import Challenge
from ludoscienceapp.utils.System import System
from ludoscienceapp.models.badge import Badge
from django.contrib import messages
from ludoscienceapp.forms import BadgeForm
import os




def badge(request):
    if System.is_logged(request):
          if System.is_admin(request):
              return render(request, 'ludoscienceapp/game_elements/create_badge.html',{'nav':'block','create_badge':System.get_navbar_color,'badges':Badge.objects.all(),'proyects':Proyect.objects.all()})

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


def process_badge(request):
    if System.is_logged(request):
          if System.is_admin(request):
              if not request.POST['name'] or not request.POST['area'] or not request.POST['proyect'] or not request.POST['time_restriction'] or not request.POST['goal']:
                  messages.error(request,'Debe ingresar todos los campos') 
                  return badge(request)               
              elif Badge.objects.filter(name__iexact=request.POST['name'],proyect=Proyect.objects.get(id__exact=request.POST['proyect'])).exists():
                  messages.error(request,'Ya hay una insignia con ese nombre') 
                  return badge(request)   
              else: 
                if request.POST['select']=='0':   
                  badge_= Badge(name=request.POST['name'],area=ProyectArea.objects.get(id__exact=request.POST['area']),time_restriction=TimeRestriction.objects.get(id__exact=request.POST['time_restriction']),goal=request.POST['goal'],owner=User.objects.get(id__exact=request.session['id']),proyect=Proyect.objects.get(id__exact=request.POST['proyect']))
                else:
                  parent_badge=Badge.objects.get(id__exact=request.POST['select'])
                  badge_= Badge(name=request.POST['name'],area=ProyectArea.objects.get(id__exact=request.POST['area']),time_restriction=TimeRestriction.objects.get(id__exact=request.POST['time_restriction']),goal=request.POST['goal'],owner=User.objects.get(id__exact=request.session['id']),proyect=Proyect.objects.get(id__exact=request.POST['proyect']),parent=parent_badge)
                badge_.save()   
                form = BadgeForm(data=request.POST, files=request.FILES, instance=badge_)
                if form.is_valid():
                    if os.path.exists(badge_.image.path):
                        os.remove(badge_.image.path)
                form.save()
              messages.success(request,'Se ha creado correctamente')
              return badge(request)   
          return redirect('home')  
    return redirect('index') 
