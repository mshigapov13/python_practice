#from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def homePageView(request):
    return HttpResponse('Hello!')

class HomePageView(TemplateView):
    template_name = 'home.html'