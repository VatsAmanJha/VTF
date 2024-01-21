from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Journal


def journal_detail(request, journal_id):
    try:
        # Try to get the current journal
        current_journal = get_object_or_404(Journal, pk=journal_id)

        # Get three journals with the same category as the current journal
        related_journals = Journal.objects.filter(
            category=current_journal.category
        ).exclude(pk=current_journal.pk)[:3]
    
        # Render the template with the current journal and related journals
        return render(
            request,
            "journal_detail.html",
            {"journal": current_journal, "related_journals": related_journals},
        )

    except Exception as e:
        # Handle the case where the blog is not found
        return HttpResponse("Blog not found", status=404)
