"""
URL configuration for techitcheap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homepage, name="homepage"),
    path("about_us/", views.about_us, name="about_us"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
    path("terms_of_use/", views.terms_of_use, name="terms_of_use"),
    path("FAQs/", views.FAQs, name="FAQs"),
    path('portfolio/', include('portfolio.urls')),
    path("contactus/", include("contactus.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)