from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *


def Home(request):
    projects = ProjectDetail.objects.all()
    template = loader.get_template('index.html')
    user = UserDetail.objects.first()
    certificates = Certificates.objects.all()
    context = {
         'user': user,
         'projects': projects,
        'certificates': certificates,
    }
    return HttpResponse(template.render(context, request))
