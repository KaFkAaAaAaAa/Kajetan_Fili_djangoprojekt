from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Note
from .forms import NoteForm
from django.contrib.auth.models import User
from django.utils.text import slugify


def note_list(request):
    all_notes_list = Note.objects.all()
    paginator = Paginator(all_notes_list, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'notes/note_list.html', {'page_obj': page_obj})


def note_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = User.objects.get(id=1)
            note.slug = slugify(form.cleaned_data['title'])
            note.save()
            return render(request, 'notes/note_form.html', {'form': form})
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})


