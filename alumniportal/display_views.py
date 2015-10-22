#####DO NOT CLOSE WINDOW
from alumniportal import forms
from alumniportal import models
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
import time

def home(request):
    return render(request,'alumniportal/main-body.html', {'page': 'home'})

def activity(request):
    return render(request,'alumniportal/activities.html', {'page': 'activity'})

def community(request):
    return render(request,'alumniportal/communities.html', {'page': 'community'})

def news(request):
    return render(request,'alumniportal/news.html', {'page': 'news'})

@login_required
def profile(request):
	profile = models.Profile.objects.get(user = request.user)
	return render(request,'alumniportal/profile.html', {
    	'page': 'profile',
    	'profile':profile,
    	})

def news_list(request):
    return render(request,'alumniportal/news-list.html', {'page': 'news-list'})
