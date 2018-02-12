# -*- coding: utf-8 -*-
import os

from django.conf import settings
from django.shortcuts import render
from uploads.models import Upload


def get_index(request):
    uploads = Upload.objects.all()
    media_url = os.path.join(settings.AWS_S3_CUSTOM_DOMAIN,
                             settings.MEDIAFILES_LOCATION)
    print(media_url)
    return render(
        request, 'home/index.html',
        {'uploads': uploads, 'media_url': media_url})


# Display all the uploads
"""
def listing(request):


        retrieve all uploads and display as a list
    :param request:
    :return:
"""
