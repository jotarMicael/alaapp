
from django.shortcuts import render
from ludoscienceapp.models.proyect import Proyect
from ludoscienceapp.utils.System import System

def view_game_elements(request,ok=False):  
    if System.is_logged(request):
          if System.is_player(request):
              if not ok:
                proyect=Proyect.objects.get(id__exact=request.POST['id'])   
              else:
                proyect=Proyect.objects.get(id__exact=ok)
              return render(request, 'ludoscienceapp/game_elements/views_game_elements.html',{'nav':'block','create_badge':System.get_navbar_color,'badges':proyect.get_badges_not_exists_user(request.session['id']),'challenges':proyect.get_challenges_not_exists_user(request.session['id']),'name':proyect.get_name() }) 