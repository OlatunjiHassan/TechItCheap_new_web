from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.portfolio_index, name="portfolio_index"),
    path('search/', views.search, name='search'),
    path('<int:pk>/', views.project_details, name='project_details'),
    path('category/<str:option>', views.category, name='category')
]