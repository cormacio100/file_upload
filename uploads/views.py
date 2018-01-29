# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def upload_form(request):
    return render(request, 'uploads/upload_form.html')