# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

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



import os

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
	    	 profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )



def userlogin(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
		args = {'user':user}
                return render(request, 'welcome.html', args)
        else:
            return render(request, 'login.html', {})

    else:
        return render(request, 'login.html', {})




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
    lim =[]
    lip =[]
    c_user = request.user
    music = MusicCollection.objects.filter(Q(user = c_user))
    for i in music:
	lim.append(i)
    pictures = UserProfile.objects.filter(Q(user = c_user))
    for i in pictures:
	lip.append(i)
    return render_to_response(request, 'welcome.html',{'lim': lim, 'lip':lip})


@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def playlist(request):
    return render(request, 'playlist.html', {'form': form})
    
