from django.urls import path
from .views import network_graph
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('network-graph/', network_graph, name='network_graph'),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
