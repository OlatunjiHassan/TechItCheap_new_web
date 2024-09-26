from django.shortcuts import render

def homepage(request):
    return render(request, "homepage.html")

def privacy_policy(request):
    return render(request, "privacy_policy.html")

def about_us(request):
    return render(request, "about_us.html")

def terms_of_use(request):
    return render(request, "terms_of_use.html")

def FAQs(request):
    return render(request, "FAQs.html")