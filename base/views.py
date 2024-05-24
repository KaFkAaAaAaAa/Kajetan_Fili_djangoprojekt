from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Note


def note_list(request):
    all_notes_list = Note.objects.all()
    paginator = Paginator(all_notes_list, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'notes/note_list.html', {'page_obj': page_obj})


def note_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})
