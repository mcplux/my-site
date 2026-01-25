from django.shortcuts import render
from django.http import Http404
from .models import Home


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
