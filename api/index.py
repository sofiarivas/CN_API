from django.contrib.algoliasearch import AlgoliaIndex

class ColorIndex(AlgoliaIndex):
    
    fields = 'name', 'descripcion'
    settings = {'attributesToIndex': ('name','descripcion')}
