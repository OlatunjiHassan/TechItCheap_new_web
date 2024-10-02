from django.shortcuts import render
from portfolio.models import Project
from .forms import SearchForm

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

def search(request):
    form = SearchForm(request.GET or None)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']

        r_title = Project.objects.filter(title__icontains = query)
        for obj in r_title:
            results.append(obj)
        r_category = Project.objects.filter(category__icontains = query)
        for obj in r_category:
            results.append(obj)
        r_desc= Project.objects.filter(description__icontains = query)
        for obj in r_desc:
            results.append(obj)
                        
    context = {'form':form, 'results':results}
    return render(request, 'portfolio/search.html', context)