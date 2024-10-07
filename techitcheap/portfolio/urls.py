from django.urls import path
from .views import ProjectListView, ProjectCategoryView, ProjectDetailView, ProjectSearchView

app_name = "portfolio"

urlpatterns = [
    path("", ProjectListView.as_view(), name="portfolio_index"),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_details'),
    path('category/<str:option>', ProjectCategoryView.as_view(), name='category'),
    path('search/', ProjectSearchView.as_view(), name='search'),
]