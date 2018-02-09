# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,  redirect

# Create your views here.

from musa.models import UserProfile, MusicCollection

from django.conf import settings

from musa.forms import UserProfileForm, MusicForm, ContactForm

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.db.models import Q

from django.views import View

import smtplib
import unicodedata
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage


import os



def homepage(request):
    return render(request, 'index.html', context=None)

def contactpage(request):
    form=ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            sender = "sweettunes@gmail.com"
            receiver = "ccsreenidhin@gmail.com"
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.starttls()
            smtpObj.login(sender, "1234!@#$")
            receiver = unicodedata.normalize('NFKD', receiver).encode('ascii','ignore')
            message = u'<ul><li>name:'+name+u'</li><li>email:'+email+u'</li><li>content:'+content+u'</li></ul>'
            msg = MIMEText(message,'html')
            msg['Subject'] = "SweetTunes"
            msg['From'] = sender
            msg['To'] = receiver
            smtpObj.sendmail(sender, receiver, msg.as_string())
            return redirect('/thanks/')
    return render(request, 'contact.html', {'form':form})

def aboutpage(request):
    return render(request, 'about.html', context=None)

def downloadpage(request):
    return render(request, 'download.html', context=None)

def thankspage(request):
    return render(request, 'thanks.html', context=None)
    
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
    musics_list={}
    pics = {}
    try:
        pics = UserProfile.objects.get(user=request.user, user__is_active = True)
    except:
        pass
    try:
        musics_list = MusicCollection.objects.filter(user=request.user, user__is_active = True)
    except:
        pass
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            print "hi"
            music = form.save(commit=False)
            music.user = request.user
            music.save()
            data = {'is_valid': True, 'name': music.document.name, 'url':music.document.url}
        else:
            data = {'is_valid': False}
            return JsonResponse(data)
    return render(request, 'collections.html', {'pics':pics, 'musics':musics_list})


@login_required
def clear_database(request):
    for music in MusicCollection.objects.filter(user=request.user, user__is_active = True):
        music.document.delete()
        music.delete()
    return redirect(request.POST.get('next'))


@login_required
def profedit(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    form = UserProfileForm(instance = profile)
    try:
        pics = UserProfile.objects.get(user=request.user, user__is_active = True)
    except:
        pics={}
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponseRedirect('/profedit/')
    return render(request, 'profile.html', {'form': form, 'pics':pics})


@login_required
def musicdelete(request, pk):
    music = MusicCollection.objects.filter(user=request.user, user__is_active = True).get(pk=pk)
    music.document.delete()
    music.delete()
    return HttpResponseRedirect('/welcome/')

    
