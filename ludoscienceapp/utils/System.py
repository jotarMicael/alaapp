from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import logout
from django.template.loader import render_to_string
from ludoscienceapp.models.token import Token
from werkzeug.security import generate_password_hash,check_password_hash
from decouple import config

import hashlib
import random
class System(object):
    
    
    @staticmethod
    def is_logged(request):
        try:
            request.session['id']
        except KeyError:
            return False     
        else:
            return True


    @staticmethod
    def f_send_mail(user):
        token = System.generate_token()
        encript = generate_password_hash(str(user.id), 'sha256', 5)
        t=Token(user_id=user,token=token)
        t.save()
        message_ = render_to_string(
            'ludoscienceapp/verificate/activate_account.html',
            { 'token': token+encript,'site': config('DEFAULT_DOMAIN') }
            )
        subject="Bienvenido/a a CienciaCRE"
        message=''
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[user.email]
        html_message=message_
        #send_mail(subject,message,email_from,recipient_list,fail_silently=False,html_message)
        send_mail(
            subject=subject, 
            message=message, 
            recipient_list=recipient_list, 
            from_email=email_from, 
            fail_silently=False,
            html_message=html_message
            )

    @staticmethod
    def set_session(request,user):
        try:
            request.session['profile_image'] = user.profile_image.url   
        except ValueError:
            pass
        finally:
            request.session['id'] = user.id 
            request.session['username'] = user.username 
            request.session['email'] = user.email
            request.session['complete_name'] = user.complete_name 
            request.session['role'] = user.role_id.name
    @staticmethod
    def logout(request):
        
        try:
            del request.session['id']
        except KeyError:
            return False  
    

    @staticmethod
    def generate_token(length=15):
        chars = list(
        'ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwyz01234567890'
        )
        random.shuffle(chars)
        chars = ''.join(chars)
        sha1 = hashlib.sha1(chars.encode('utf8'))
        token = sha1.hexdigest()
        return token[:length]   

    def decode_token(token,user_id):
        object_token=Token.objects.get(token__iexact=token)
       
        if check_password_hash(user_id,str(object_token.user_id.id)):
            #check_password_hash(user.password,request.POST['password'])
            return object_token.user_id.id
        return None
    def is_admin(request):
        return (request.session['role']=='ADMIN')

    def is_root(request):
        return (request.session['role']=='ROOT')  

    def is_player(request):
        return (request.session['role']=='PLAYER')  


    @staticmethod
    def get_navbar_color():
        return settings.NAVBAR_COLOR
  