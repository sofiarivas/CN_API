from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import viewsets
from .models import Color
from .serializers import ColorSerializer
# Create your views here.

# Esto es un Viewset


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class DisplayColors(View):
    def get(self, request):
        template_name = 'api/display_advanced.html'
        return render(request, template_name)

class SearchColors(TemplateView):
    template_name = 'api/search.html'

def index(request):
    return HttpResponse("INDEX")


class HomeView(View):
    def get(self, request):
        response = HttpResponse('{"response": "Esto es my home"}', content_type='application/json')
        response.content_type = 'application/json'
        return response

class IndexView(View):

    def get(self, request):
        get_params = request.GET
   
        nombre= get_params.get("nombre", "Fulano")
        # print(dir(request))
        return HttpResponse("<h1>Hola " + nombre + "<h1>")

    @method_decorator(csrf_exempt)
    def post(self, request):
        get_params = request.POST
        nombre= get_params.get("nombre", "Fulano")
        return HttpResponse("Método POST llamado por" + nombre)


class GreetView(View):
    def get(self, request, nombre, apellido):
        return HttpResponse("<h1> Hola " + nombre + " " + apellido + " <h1>")

class JsonView(View):
    """
    Esta vista intenta rederizar un json
    """
    def get(self, request, color):
        return HttpResponse("""
            {"grupo": "Cinta negra",
                "integrantes": ["Salvador", "Ivan", "Hector"]
                }
            """, content_type='application/json')

    def post(self, request, color):
        colores = {
            'rojo': '#FF0000',
            'azul': '#0000FF'
        }

        my_json = {
            'colors' : [
                '#000000',
                '#FFFFFF',
                '#FF0000',
                '#00FF00',
                '#0000FF'
            ]
        }
        body = request.body
        print(body[1:])
        myobject = json.loads(body.decode('ascii'))
        print(myobject)
        my_json["colors"].append(color)

        return HttpResponse(json.dumps(my_json), content_type='application/json' )


class ColorView(View):
    colores = {
        'rojo': '#FF0000',
        'azul': '#0000FF'
    }
    def get(self, request, color):
        hex = self.colores.get(color)
        if hex:
            resp = { 'status': 'ok', 'hex': hex }
        else:
            resp = { 'status': 'error', 'message': 'Color not available'}

        return HttpResponse(json.dumps(resp), content_type='application/json')


class ColorV(View):
    def get(self, request):
        colors = Models.Colors.objects.all()
        return colors