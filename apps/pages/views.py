from django.shortcuts import render
from django.http import Http404
from .models import Home, About


def home(request):
    home_page = Home.objects.first()
    if home_page is None:
        raise Http404("The requested resource was not found")

    social_links = home_page.social_links.all()
    context = {
        "name": home_page.name,
        "occupation": home_page.occupation,
        "image": home_page.image,
        "social_links": social_links,
    }

    return render(request, "pages/index.html", context)


def about(request):
    about_page = About.objects.first()
    if about_page is None:
        raise Http404("The requested resource was not found")

    context = {
        "title": about_page.title,
        "content": about_page.content,
    }

    return render(request, "pages/about.html", context)
