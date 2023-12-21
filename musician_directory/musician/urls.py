from django.urls import path
from . import views

urlpatterns = [
    path('', views.MusiciansListView.as_view(), name='musicians_list'),
    path('add/', views.AddMusicianView.as_view(), name='add_musician'),
    path('edit_musician/<int:pk>/', views.EditMusicianView.as_view(), name='edit_musician'),
    path('musician_detail/<int:pk>/', views.MusicianDetailView.as_view(), name='musician_detail'),
    path('<int:musician_id>/delete/', views.DeleteMusicianView.as_view(), name='delete_musician'),
]
