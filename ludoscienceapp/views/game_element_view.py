
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from ludoscienceapp.models.proyect import Proyect
import json
class GameElementView(TemplateView):
    template_name = 'create_challenge.html'

    @method_decorator(csrf_exempt)
   
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    @csrf_exempt
    def post(self, request, *args, **kwargs):

        data = []
        data_time_restriction = []     
        data_area = []  
        data_subarea = []  
        try:
            action = request.POST['action']
            if action == 'search_time_restriction_id':
                proyect=Proyect.objects.get(id=int(request.POST['id']))      
                for i in proyect.time_restriction.all():
                    data_time_restriction.append({'id': i.id, 'name': i.name})          
                data_area.append({'id': i.id, 'name': proyect.area.name})
                
                for subarea in proyect.area.proyectsubarea_set.all():
                    data_subarea.append({'id': subarea.id, 'subarea': json.loads(subarea.sub_area)['geometry']['coordinates'] })
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        data.append(data_time_restriction)
        data.append(data_area)
        data.append(data_subarea)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Aninados | Django'
        
        return context