
from django.shortcuts import render
from ludoscienceapp.models.project import Project
from ludoscienceapp.models.challenge import Challenge
from ludoscienceapp.models.game_element import GameElement
from ludoscienceapp.views.project import game_elements_project
from django.contrib import messages
from ludoscienceapp.models.badge import Badge
from ludoscienceapp.models.user import User
from ludoscienceapp.utils.System import System

def view_game_elements(request,ok=False):  
    if System.is_logged(request):
          if System.is_player(request):
              if not ok:
                project=Project.objects.get(id__exact=request.POST['id'])   
              else:
                project=Project.objects.get(id__exact=ok)
              return render(request, 'ludoscienceapp/game_elements/views_game_elements.html',{'nav':'block','view_game_elements':System.get_navbar_color,'badges':Badge.objects.filter(project=project).exclude(user_actives = User.objects.get(id=request.session['id'])).all(),'challenges':Challenge.objects.filter(project=project).exclude(user_actives = User.objects.get(id=request.session['id'])).all(),'name':project.get_name() }) 

def change_state(request):
    if System.is_logged(request):
          if System.is_admin(request):
            ge=GameElement.objects.get_subclass(id=request.POST['ge_id'])
            ge.change_state()     
            messages.success(request,' %s  %s con éxito'  % (ge.get_name(),ge.get_state()))
            return game_elements_project(request,ge.project_id)

def modify(request,ok=False):
  if System.is_logged(request):
        if System.is_admin(request):
          if not ok:
            id_= request.POST['ge_id_']
          else:
            id_=request.POST['id']
          ge=GameElement.objects.get_subclass(id=id_)
          areas=ge.project.area.projectsubarea_set.all()
          time_restrictions=ge.project.time_restriction.all()
          if isinstance(ge, Challenge):
            return render(request, 'ludoscienceapp/game_elements/modify_challenge.html',{'nav':'block','modify_challenge':System.get_navbar_color,'challenge':ge, 'areas':areas,'time_restrictions':time_restrictions}) 
          return render(request, 'ludoscienceapp/game_elements/modify_badge.html',{'nav':'block','modify_badge':System.get_navbar_color,'badge':ge,'areas':areas,'time_restrictions':time_restrictions}) 