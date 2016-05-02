from django.conf.urls import url
from .views import IndexView, GreetView, JsonView, ColorView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # url(r'index/$', IndexView.as_view()), # varias urls
    url(r'index$', csrf_exempt(IndexView.as_view())), # varias urls
    url(r'greet/([a-z]+)/([a-zA-Z]+)$', csrf_exempt(GreetView.as_view())), # varias urls
    url(r'json/([a-z]+)/$', csrf_exempt(JsonView.as_view())),
    url(r'color/([a-z]+)/$', csrf_exempt(ColorView.as_view()))
    # url(r'index/$', IndexView.as_view()), # varias urls
    ]








