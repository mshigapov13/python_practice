from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response


def index(request):
    return HttpResponse('Hello world!')
'''
def index(request):
    template = loader.get_template('xsstest/hello.html')
    name = request.GET.get('name', 'world')
    return HttpResponse(template.render(name, request))
'''

def notsecure(request):
    
    name = request.GET.get('name', 'world')
    return render_to_response('xsstest/hello.html', {'name':name})