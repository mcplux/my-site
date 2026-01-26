from django.shortcuts import render, redirect
from django.http import Http404
from django.db import DatabaseError
from .models import Home, About, Portfolio, Contact
from .forms import ContactForm
from apps.contact.models import ContactMessage


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


def portfolio(request):
    portfolio_page = Portfolio.objects.first()
    if portfolio_page is None:
        raise Http404("The requested resource was not found")

    context = {
        "title": portfolio_page.title,
        "projects": portfolio_page.projects.all(),
    }

    return render(request, "pages/portfolio.html", context)


def contact(request):
    contact_page = Contact.objects.first()
    if contact_page is None:
        raise Http404("The requested resource was not found")

    success_message = None

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                ContactMessage.objects.create(
                    name=form.cleaned_data["name"],
                    email=form.cleaned_data["email"],
                    message=form.cleaned_data["message"],
                )
                success_message = "Message sent successfully"
                form = ContactForm()
                redirect("contact")

            except DatabaseError as e:
                print(e)
                form.add_error(None, "Something went wrong. Please try again later")
    else:
        form = ContactForm()

    context = {
        "title": contact_page.title,
        "form": form,
        "success_message": success_message,
    }

    return render(request, "pages/contact.html", context)
