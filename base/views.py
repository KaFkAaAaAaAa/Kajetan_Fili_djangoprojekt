from django.shortcuts import render, get_object_or_404
from .models import Note


def notes_list(request):
    notes = Note.published.all()
    return render(request, 'base/templates/notebook/note/list.html', {'notes': notes})


def note_detail(request, year, month, day, note):
    note = get_object_or_404(Note, slug=note,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'base/templates/notebook/note/detail.html', {'note': note})
