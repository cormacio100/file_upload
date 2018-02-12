# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
import os


def profile_image_path(instance, filename):
    upload_dir = os.path.join('profile/', instance.description)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)


class Upload(models.Model):

    def __unicode__(self):
        return self.name

    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='no_image.png'
    )
    document = models.FileField(
        upload_to='documents/',
        default='no_text.txt'
    )
    uploaded_at = models.DateTimeField(
        default=datetime.now
    )
