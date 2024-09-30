from django.urls import path
from .views import contact_view

app_name = "contactus"

urlpatterns = [
    path("contactus/", contact_view, name='contactus')
]