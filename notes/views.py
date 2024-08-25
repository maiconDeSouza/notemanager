from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from notes.models import Note
# Create your views here.


class NotesList(ListView):
    model = Note


class CreateNote(CreateView):
    model = Note
    fields = ['title', 'description', 'important']
    success_url = reverse_lazy('note_list')


class DetailNote(DetailView):
    model = Note


class DeleteNote(DeleteView):
    model = Note
    success_url = reverse_lazy('note_list')


class UpdateNote(UpdateView):
    model = Note
    fields = ['title', 'description', 'important']
    success_url = reverse_lazy('note_list')
