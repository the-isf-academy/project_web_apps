from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone


#### class based views

# homepage
def index(request):
    response = render(request, 'myapp/index.html')
    return response