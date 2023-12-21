from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Album
from .forms import AlbumForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album/add_album.html'
    success_url = reverse_lazy('musicians_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response if self.request.method == 'POST' else redirect(self.success_url)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album/album_details.html'
    context_object_name = 'album'
    pk_url_kwarg = 'album_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    pk_url_kwarg = 'album_id'
    template_name = 'album/edit_album.html'

    def get_success_url(self):
        return reverse_lazy('album_detail', kwargs={'album_id': self.object.pk})

class DeleteAlbumView(DeleteView):
    model = Album
    context_object_name = 'album'
    pk_url_kwarg = 'album_id'
    success_url = reverse_lazy('musicians_list')