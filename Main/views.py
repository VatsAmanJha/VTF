from django.shortcuts import render
from Content.models import Journal


def index(request):
    banner_url = "/media/banner.png"
    logo_url = "/media/logo.png"
    latest_journals = Journal.objects.all()[:3]

    return render(
        request,
        "index.html",
        {
            "banner_url": banner_url,
            "logo_url": logo_url,
            "latest_journals": latest_journals,
        },
    )


def about(request):
    logo_url = "/media/logo.png"
    banner_url = "/media/banner_about.jpg"
    about_url = "/media/about.jpg"
    return render(
        request,
        "about.html",
        {
            "banner_url": banner_url,
            "about_url": about_url,
            "logo_url": logo_url,
        },
    )


def contact(request):
    logo_url = "/media/logo.png"  # Replace with the actual path to your logo image
    banner_url = (
        "/media/banner_about.jpg"  # Replace with the actual path to your banner image
    )

    return render(
        request, "contact.html", {"logo_url": logo_url, "banner_url": banner_url}
    )


def journal(request):
    latest_journals = Journal.objects.all()
    logo_url = "/media/logo.png"
    banner_url = "/media/banner_about.jpg"
    return render(
        request,
        "journal.html",
        {
            "latest_journals": latest_journals,
            "banner_url": banner_url,
            "logo_url": logo_url,
        },
    )
