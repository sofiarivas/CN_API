from django.apps import AppConfig
from django.contrib import algoliasearch
from .index import ColorIndex
    

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        Color = self.get_model('color')
        algoliasearch.register(Color, ColorIndex)
