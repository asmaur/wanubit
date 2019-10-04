from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    projects = Project.objects.all()
    return render(request, "wanu/index.html", {"projects": projects})