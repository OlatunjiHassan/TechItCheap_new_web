from django.shortcuts import render
from portfolio.models import Project
# from .forms import SearchForm
from rest_framework import generics, permissions
from .serializers import ProjectSerializer
from django.db.models import Q

#This means that it is impossible to edit from client. It is only editable through django admin interface
class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

#This view is the portfolio page. It returns a list of all existing in the database
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all().order_by("-date")
    serializer_class = ProjectSerializer
    permission_classes = [ReadOnly]

#This view is for each category. It returns a list of item whose category is the chosen option
class ProjectCategoryView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    def get_queryset(self):
        category = self.kwargs['option']
        return Project.objects.filter(category=category).order_by("-date")


#This view is for each item in the database. It returns the item whose id is specified
class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


#This view is for the search functionality. It returns a list of all items whose title, category or description is matched by the query
class ProjectSearchView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        return Project.objects.filter(
            Q(title__icontains=query) |
            Q(category__icontains=query) |
            Q(description__icontains=query)
        ).order_by('-date')
    






# def portfolio_index(request):
    
#     projects = Project.objects.all().order_by("-date")
#     context = {
#         "projects":projects
#     }
#     return render(request, 'portfolio/portfolio.html', context)

# def category(request, option):
#     options = ["Website Design", "Product Development", "Mobile app development", "mobile app and web maintanance"]
#     for opt in options:
#         if opt == option:
#             projects = Project.objects.filter(category=option).order_by("-date")
#             context = {"projects":projects, "option":option}
#             return render(request, "portfolio/categories.html", context)
#         else:
#             continue

# def project_details(request, pk):
#     project = Project.objects.get(pk=pk)
#     context = {
#         "project":project
#     }
#     return render(request, "portfolio/project_details.html", context)

# def search(request):
#     form = SearchForm(request.GET or None)
#     results = []
#     if form.is_valid():
#         query = form.cleaned_data['query']

#         r_title = Project.objects.filter(title__icontains = query)
#         for obj in r_title:
#             results.append(obj)
#         r_category = Project.objects.filter(category__icontains = query)
#         for obj in r_category:
#             results.append(obj)
#         r_desc= Project.objects.filter(description__icontains = query)
#         for obj in r_desc:
#             results.append(obj)
                        
#     context = {'form':form, 'results':results}
#     return render(request, 'portfolio/search.html', context)