from django.conf.urls import url, include
# from .views import IndexView, GreetView, JsonView, ColorView, ColorViewSet
from django.views.decorators.csrf import csrf_exempt
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'colors', views.ColorViewSet)

urlpatterns = [
	url(r'^search/$', views.SearchColors.as_view(),name="search"),
    url(r'^display/$', views.DisplayColors.as_view(), name="display"),
    url(r'^', include(router.urls)),
    
]

    # url(r'index/$', IndexView.as_view()), # varias urls
    # url(r'index$', csrf_exempt(IndexView.as_view())), # varias urls
    # url(r'greet/([a-z]+)/([a-zA-Z]+)$', csrf_exempt(GreetView.as_view())), # varias urls
    # url(r'json/([a-z]+)/$', csrf_exempt(JsonView.as_view())),
    # url(r'color/([a-z]+)/$', csrf_exempt(ColorView.as_view()))
    # url(r'index/$', IndexView.as_view()), # varias urls








