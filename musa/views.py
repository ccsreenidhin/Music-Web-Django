# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from .models import UserProfile

from django.conf import settings

from musa.forms import UserProfileForm, MusicForm, UserForm

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required

from musa.models import UserProfile, MusicCollection

from django.contrib.auth.models import User

from django.db.models import Q

from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test




import os




def fileupload(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MusicForm()
    return render(request, 'welcome.html', {
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


def downloadapp(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "application/musiana.tar.gz")
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


@login_required
def userpage(request):
    posts = {}
    if request.user.is_authenticated():
       posts = UserProfile.objects.get(user=request.user, user__is_active = True)
    return render(request, 'welcome.html', {'posts': posts})



@login_required
def playlist(request):
    return render(request, 'playlist.html', {'form': form})
    
