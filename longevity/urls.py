from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('homepage/', views.index, name='homepage'),
    path('sbha/', views.sbha, name='sbha'),
]

