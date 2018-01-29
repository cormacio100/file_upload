# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from forms import FileUploadForm
from django.core.files.storage import FileSystemStorage

# Create your views here.
def upload_form(request):
    if request.method=='POST' and request.FILES['myfile']:
        #   retrieve the file obj
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        uploaded_file_url = fs.url(filename)
        form = FileUploadForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully registered as an Entertainer")
            return render(request,
                          'uploads/upload_form.html',
                          {'uploaded_file_url': uploaded_file_url})
    else:
        #   If page was just loaded then an empty form is displayed
        form = FileUploadForm(request.user)
    return render(request, 'uploads/upload_form.html',{'form':form})