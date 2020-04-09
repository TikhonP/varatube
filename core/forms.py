from django import forms
from .models import Files


class UploadForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['name', 'discription', 'file']
