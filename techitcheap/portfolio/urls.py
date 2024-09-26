from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.portfolio, name="portfolio"),
    # path("mobile_app/", views.mobile_app, name="mobile_app"),
    # path("brand_design/", views.brand_design, name="brand_design"),
    # path("website_design/", views.website_design, name="website_design"),
    # path("product_dev/", views.product_dev, name="product_dev"),
]