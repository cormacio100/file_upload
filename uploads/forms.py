from django import forms
from uploads.models import Upload
import os

class DocumentImageForm(forms.ModelForm):
    #   Tell Django which model to used to create the form
    class Meta:
        model = Upload
        fields = ('description', 'image', 'document',)
