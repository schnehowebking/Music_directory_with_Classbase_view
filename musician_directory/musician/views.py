from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Musician
from album.models import Album
from .forms import MusicianForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

class MusiciansListView(ListView):
    model = Musician
    template_name = 'musician/index.html'
    context_object_name = 'musicians'

class AddMusicianView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician/addmusician.html'
    success_url = reverse_lazy('add_album')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response if self.request.method == 'POST' else redirect(self.success_url)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    
class MusicianDetailView(DetailView):
    model = Musician
    template_name = 'musician/musicians_details.html'
    context_object_name = 'musician'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.filter(musician=self.object)
        return context

class EditMusicianView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician/edit_musician.html'

    def get_success_url(self):
        return reverse_lazy('musician_detail', kwargs={'pk': self.object.pk})

class DeleteMusicianView(DeleteView):
    model = Musician
    template_name = 'musician/delete_musician.html'
    pk_url_kwarg = 'musician_id'
    success_url = reverse_lazy('musicians_list')