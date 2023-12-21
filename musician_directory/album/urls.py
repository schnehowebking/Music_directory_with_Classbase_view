from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddAlbumView.as_view(), name="add_album"),
    path('album/album_detail/<int:album_id>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('edit_album/<int:album_id>/', views.EditAlbumView.as_view(), name='edit_album'),
    path('delete_album/<int:album_id>/', views.DeleteAlbumView.as_view(), name='delete_album'),
]
