from django.shortcuts import render, redirect
from django.http import Http404
from django.db import DatabaseError
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import Home, About, Portfolio, Contact
from .forms import ContactForm
from apps.contact.models import ContactMessage


@require_http_methods(["GET"])
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


@require_http_methods(["GET"])
def about(request):
    about_page = About.objects.first()
    if about_page is None:
        raise Http404("The requested resource was not found")

    context = {
        "title": about_page.title,
        "content": about_page.content,
    }

    return render(request, "pages/about.html", context)


@require_http_methods(["GET"])
def portfolio(request):
    portfolio_page = Portfolio.objects.first()
    if portfolio_page is None:
        raise Http404("The requested resource was not found")

    context = {
        "title": portfolio_page.title,
        "projects": portfolio_page.projects.all(),
    }

    return render(request, "pages/portfolio.html", context)


@require_http_methods(["GET", "POST"])
def contact(request):
    contact_page = Contact.objects.first()
    if contact_page is None:
        raise Http404("The requested resource was not found")

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                ContactMessage.objects.create(**form.cleaned_data)
                messages.success(request, "Message sent successfully")
                return redirect("contact")

            except DatabaseError:
                form.add_error(None, "Something went wrong. Please try again later")
    else:
        form = ContactForm()

    context = {
        "title": contact_page.title,
        "form": form,
    }

    return render(request, "pages/contact.html", context)
