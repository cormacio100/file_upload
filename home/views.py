# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from uploads.models import Upload

# Create your views here.
def get_index(request):
    uploads = Upload.objects.all()
    return render(request, 'home/index.html',{'uploads':uploads})


# Display all the uploads
"""
def listing(request):


        retrieve all uploads and display as a list
    :param request:
    :return:
"""
