"""ludoscience URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from threading import activeCount
from ludoscienceapp.views import user, admin, proyect, game_elements, checkin
from ludoscienceapp.views.game_element_view import GameElementView
from django.urls import path

urlpatterns = [
    path('', user.index,name='index'),
    path('home/',user.home, name='home'),  
    path('logout/',user.logout, name='logout'),
    path('register/',user.register,name='register'),
    path('register_user/',user.register_user,name='register_user'),
    path('login/',user.login, name='login'), 
    path('verificate/',user.verificate, name='verificate'),
    path('activate_account/',user.activate_account,name='activate_account'),
    path('active_account/',user.active_account,name='active_account'),
    path('create_admin/',admin.create_admin,name='create_admin'),
    path('modify_proyect/',proyect.modify_proyect,name='modify_proyect'),
    path('register_admin/',admin.register_admin,name='register_admin'),
    path('create_proyect/',proyect.create_proyect,name='create_proyect'),
    path('register_proyect/',proyect.register_proyect,name='register_proyect'),
    path('edit_proyect/',proyect.edit_proyect,name='register_proyect'),
    path('create_badge/',game_elements.badge,name='create_badge'),
    path('process_badge/',game_elements.process_badge,name='process_badge'),
    path('create_challenge/',game_elements.challenge,name='create_challenge'),
    path('process_challenge/',game_elements.process_challenge,name='process_challenge'),
    path('game_element_view/',GameElementView.as_view(),name='game_element_view'),
    path('create_checkin/',checkin.checkin,name='create_checkin'),
    path('process_checkin/',checkin.process_checkin,name='process_checkin')
]



