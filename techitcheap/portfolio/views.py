from django.shortcuts import render

# Create your views here.
def portfolio(request):
    return render(request, 'portfolio.html')

# def brand_design(request):
#     return render(request, 'brand_design.html')

# def mobile_app(request):
#     return render(request, 'mobile_app.html')

# def website_design(request):
#     return render(request, 'website_design.html')

# def product_dev(request):
#     return render(request, 'product_dev.html')
