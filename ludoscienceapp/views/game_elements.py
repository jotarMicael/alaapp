
from django.shortcuts import redirect, render
from ludoscienceapp.models.user import  User 
from ludoscienceapp.models.area import Area
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
              return render(request, 'ludoscienceapp/game_elements/create_badge.html',{'nav':'block','create_badge':System.get_navbar_color,'badges':Badge.objects.all()})

def create_badge(request):
    if System.is_logged(request):
          if System.is_admin(request):
              if not request.POST['name'] or  not request.POST['datetime'] or not request.POST['lat'] or not request.POST['lon']  or not request.FILES.get('image') or not request.POST['score']:
                  messages.error(request,'Debe ingresar todos los campos')
                  return badge(request)            
              area=Area(lat=request.POST['lat'],long=request.POST['lon'])
              area.save()
              if request.POST['select']=='0':
                  badge_=Badge(name=request.POST['name'],area=area,time_restriction=request.POST['datetime'],goal=request.POST['score'],owner=User.objects.get(id__exact=request.session['id']))
              else:
                  parent_badge=Badge.objects.get(id__exact=request.POST['select'])
                  badge_=Badge(name=request.POST['name'],area=area,time_restriction=request.POST['datetime'],goal=request.POST['score'],owner=User.objects.get(id__exact=request.session['id']),parent=parent_badge)
              badge_.save()
              form = BadgeForm(data=request.POST, files=request.FILES, instance=badge_)
              if form.is_valid():
                if os.path.exists(badge_.image.path):
                        os.remove(badge_.image.path)
                form.save()
              messages.success(request,'Se ha creado correctamente')
              return badge(request)  

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
              
              challenge_=Challenge(name=request.POST['name'],area=ProyectArea.objects.get(id__exact=request.POST['area']),time_restriction=TimeRestriction.objects.get(id__exact=request.POST['time_restriction']),goal=request.POST['goal'],owner=User.objects.get(id__exact=request.session['id']))
              challenge_.save()            
              messages.success(request,'Se ha creado correctamente')
              return challenge(request) 