# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from forms import DocumentImageForm


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # If page was just loaded then an empty form is displayed
        form = DocumentImageForm()
    return render(request, 'uploads/upload_form.html', {'form': form})


