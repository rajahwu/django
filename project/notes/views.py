from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView

form .forms import NotesForm
from .models import Notes

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'fo

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    # template_name='notes/notes_detail.html'
