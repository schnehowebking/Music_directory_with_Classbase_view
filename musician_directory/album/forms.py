from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))