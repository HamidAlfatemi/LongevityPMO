from django.urls import path
#from .views import homePageView
from .views import network_graph

urlpatterns = [
#    path("", homePageView, name="home"),
    path('network-graph/', network_graph, name='network_graph'),
]
