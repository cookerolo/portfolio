from django.shortcuts import render
from .models import Project

# Create your views here.
def home(req):
    projects = Project.objects.all()
    return render(req, 'portfolio/home.html', {'projects': projects})

def error_404(request, exception):
        data = {}
        return render(request,'portfolio/404.html', data)
