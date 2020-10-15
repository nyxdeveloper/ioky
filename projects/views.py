from django.shortcuts import render
from .models import *

from django.views import View


class ProjectsView(View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, 'projects.html', {
            'projects': projects
        })


class ProjectDetail(View):
    def get(self, request, slug):
        project = Project.objects.get(slug=slug)
        return render(request, 'project-detail.html', {'project':project})
