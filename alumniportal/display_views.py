#####DO NOT CLOSE WINDOW
from alumniportal import forms
from alumniportal import models
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
######EDITED
import time

def home(request):
    return render(request,'alumniportal/main-body.html', {'page': 'home'})

def activity(request):
    return render(request,'alumniportal/activities.html', {'page': 'activity'})

def community(request):
    return render(request,'alumniportal/communities.html', {'page': 'community'})

def news(request):
    return render(request,'alumniportal/news.html', {'page': 'news'})

def profile(request):
    return render(request,'alumniportal/profile.html', {'page': 'profile'})

def news_list(request):
    return render(request,'alumniportal/news-list.html', {'page': 'news-list'})
