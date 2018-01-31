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
    #   check that the file was posted and that the FILES object contains key of image
    if request.method=='POST' and request.FILES['image']:

        #   retrieve the file obj
        image = request.FILES['image']
        document = request.FILES['document']

        """
            NEED TO USE FILESYSTEMSTORAGE TO SAVE TO CORRECT LOCATION
        """

        #   save the IMAGE to the filesystem and retrieve the URL from where it is stored
        img_folder = 'media/images/'
        fs_img = FileSystemStorage(location=img_folder,base_url='/media/images/')
        imageName = fs_img.save(image.name,image)
        uploaded_image_url = fs_img.url(imageName)

        #   save the DOCUMENT to the filesystem and retrieve the URL from where it is stored
        doc_folder = 'media/documents/'
        fs_doc = FileSystemStorage(location=doc_folder,base_url='/media/documents/')
        documentName = fs_doc.save(document.name, document)

        """
            File saves to the correct location e.g. media/documents/band.txt
            BUT
            .url is incorrect e.g. media/band.txt
        """
        uploaded_document_url = fs_doc.url(documentName)

        """
            NEED TO PASS
                uploaded_image_url
                uploaded_document_url
            TO THE FORM __INIT__ function so that it can be saved to the model
            So:
                list created containing URLs to be used as KWARGS in forms.py init function
        """
        _URL_LIST = [uploaded_image_url,uploaded_document_url]

        #form = FileUploadForm(uploaded_image_url,uploaded_document_url,request.POST)
        #form = FileUploadForm(request.user,request.POST)

        #   Declare the form to use and pass params
        form = FileUploadForm(request.user,request.POST,_urls=_URL_LIST)

        #   check the form is valid and if yes, save it
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


