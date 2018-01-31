# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,  redirect

# Create your views here.

from musa.models import UserProfile, MusicCollection

from django.conf import settings

from musa.forms import UserProfileForm, MusicForm

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.db.models import Q

from django.views import View

import os



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
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save(commit=False)
            music.user = request.user
            music.save()
            data = {'is_valid': True, 'name': music.document.name, 'url':music.document.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)

    elif request.method == 'GET':
	pics = []
        if request.user.is_authenticated():
	    try:
                pics = UserProfile.objects.get(user=request.user, user__is_active = True)
            except:
		pass
	    try:
                musics_list = MusicCollection.objects.filter(user=request.user, user__is_active = True)
            except:
		pass	
        return render(request, 'welcome.html', {'pics':pics, 'musics':musics_list,})
    return render(request, 'welcome.html', {})
    

@login_required
def clear_database(request):
    for music in MusicCollection.objects.filter(user=request.user, user__is_active = True):
        music.document.delete()
        music.delete()
    return redirect(request.POST.get('next'))
    



@login_required
def profileview(request):
    pics =[]
    if request.user.is_authenticated():
	try:
           pics = UserProfile.objects.get(user=request.user, user__is_active = True)
	except:
	   pass
    return render(request, 'profile.html', {'pics': pics})



@login_required
def profedit(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponseRedirect('/profile/')
    	return render(request, 'profile.html', {})
    
    elif request.method == 'GET':
	form = UserProfileForm()
        return render(request, 'profedit.html', {'form': form,})


@login_required
def musicdelete(request, pk):
    for music in MusicCollection.objects.filter(user=request.user, user__is_active = True):
	music.document.delete()
        music.delete()
    return HttpResponseRedirect('/welcome/')

