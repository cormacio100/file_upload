# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage

from uploads.models import Upload
from forms import FileUploadForm,DocumentImageForm


from django.contrib import messages
from django.core.urlresolvers import reverse


# Create your views here.
def upload_form(request):
    if request.method=='POST' and request.FILES['image']:
        #   retrieve the file obj
        image = request.FILES['image']
        document = request.FILES['document']
        fs = FileSystemStorage()
        imageName = fs.save(image.name,image)
        uploaded_image_url = fs.url(imageName)
        documentName = fs.save(document.name, document)
        uploaded_document_url = fs.url(documentName)

        """
            NEED TO PASS
            uploaded_image_url
            uploaded_document_url
            TO THE FORM __INIT__ function so that it can be saved

        """
        _URL_LIST = [uploaded_image_url,uploaded_document_url]

        #form = FileUploadForm(uploaded_image_url,uploaded_document_url,request.POST)
        #form = FileUploadForm(request.user,request.POST)
        form = FileUploadForm(request.user,request.POST,_urls=_URL_LIST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully registered as an Entertainer")
            return render(request,
                          'uploads/upload_form.html',
                          {'uploaded_image_url': uploaded_image_url,
                           'uploaded_document_url':uploaded_document_url})
    else:
        #   If page was just loaded then an empty form is displayed
        form = FileUploadForm(request.user)
    return render(request, 'uploads/upload_form.html',{'form':form})

# Create your views here.
def model_form_upload(request):
    if request.method=='POST':
        form = DocumentImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        #   If page was just loaded then an empty form is displayed
        form = DocumentImageForm()
    return render(request, 'uploads/upload_form.html',{'form':form})


