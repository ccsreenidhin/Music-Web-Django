# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from genfier.models import Document
from genfier.forms import DocumentForm
import os
from django.http import Http404, HttpResponse


def fileupload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'fileupload.html', {
        'form': form
    })

def homepage(request):
    return render(request, 'index.html', context=None)

def contactpage(request):
    return render(request, 'contact.html', context=None)

def aboutpage(request):
    return render(request, 'about.html', context=None)

def downloadpage(request):
    return render(request, 'download.html', context=None)

def userpage(request):
    return render(request, 'welcome.html', context=None)


def downloadapp(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "application/musiana.tar.gz")
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
