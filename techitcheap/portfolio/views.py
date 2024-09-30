from django.shortcuts import render
from portfolio.models import Project

# Create your views here.
def portfolio_index(request):
    projects = Project.objects.all().order_by("-date")
    context = {
        "projects":projects
    }
    return render(request, 'portfolio/portfolio.html', context)

def category(request, option):
    options = ["Website Design", "Product Development", "Mobile app development", "mobile app and web maintanance"]
    for opt in options:
        if opt == option:
            projects = Project.objects.filter(category=option).order_by("-date")
            context = {"projects":projects, "option":option}
            return render(request, "portfolio/categories.html", context)
        else:
            continue

def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project":project
    }
    return render(request, "portfolio/project_details.html", context)

