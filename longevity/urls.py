from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='homepage'),
    path('index/', views.index, name='index'),
    path('sbha/', views.sbha, name='sbha'),
    path('containerlist/', views.containerlist, name='containerlist'),
    path('process_selected_containers/', views.process_selected_containers, name='process_selected_containers'),
    path('legend/', views.legend, name='legend'),
    path('node_to_node/', views.node_to_node, name='node_to_node'),
    path('one_node/', views.one_node, name='one_node'),
]

