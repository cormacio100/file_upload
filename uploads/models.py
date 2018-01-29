# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Upload(models.Model):
    description = models.CharField(max_length=255, blank=True)
    myfile = models.ImageField(
        upload_to = 'images/',
        blank=True,
        null=True,
    )
    document = models.FileField(
        upload_to = 'documents/',
        blank = True,
        null = True
    )
    uploaded_at = models.DateTimeField(
        default = datetime.now
    )
