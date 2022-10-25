from email import message
from tokenize import PseudoExtras
from django.shortcuts import redirect, render
from creativescienceapp.models import Proyect, User, Role, GameElement
from creativescienceapp.utils.System import System
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from creativescienceapp.forms import ProyectForm
from django.conf import settings
import os


def badge(request):
    if System.is_logged(request):
          if System.is_admin(request):
              return render(request, 'creativescienceapp/game_elements/create_badge.html',{'nav':'block','create_badge':System.get_navbar_color})


def challenge(request):
    if System.is_logged(request):
          if System.is_admin(request):
              return render(request, 'creativescienceapp/game_elements/create_challenge.html',{'nav':'block','create_challenge':System.get_navbar_color})