from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Theory

def testing(request):
  mydata = Theory.objects.all()
  template = loader.get_template('template.html')
  context = {
    'theoriesofaging': mydata,
  }
  return HttpResponse(template.render(context, request))  # Return the response here

def homePageView(request):
  return testing(request)  # Call the testing function here # HttpResponse(template.render(context, request))
  