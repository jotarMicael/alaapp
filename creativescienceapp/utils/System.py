from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

class System(object):
    @classmethod
    def __init__(self):
        pass

    @staticmethod
    def is_logged(request):
        try:
            request.session['id']
        except KeyError:
            return False     
        return True


    @staticmethod
    def f_send_mail(user):
        subject="Bienvenido/a a CienciaCRE"
        message="Su código es: 1234"
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[user.email]
        send_mail(subject,message,email_from,recipient_list)

    @staticmethod
    def set_session(request,user):
        request.session['id'] = user.id 
        request.session['username'] = user.username 
        request.session['complete_name'] = user.complete_name 
        request.session['profile_image'] = user.profile_image.url   
        request.session['role'] = user.role_id.name
    @staticmethod
    def logout(request):
        try:
            del request.session['id']
        except KeyError:
            pass
        