from django.shortcuts import render
from .models import Note

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})
