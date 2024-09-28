from django.shortcuts import render
from portfolio.models import Project

# Create your views here.
def portfolio_index(request):
    projects = Project.objects.all()
    context = {
        "projects":projects
    }
    return render(request, 'portfolio/portfolio.html', context)

def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project":project
    }
    return render(request, "portfolio/project_details.html", context)

def category(request, choice):
    project = Project.objects.filter()