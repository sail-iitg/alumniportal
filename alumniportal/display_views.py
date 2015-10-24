#####DO NOT CLOSE WINDOW
from alumniportal import forms
from alumniportal import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
import time
from datetime import datetime
from constants import *

####To pass the required recent objects in required numbers
def get_recent_objects():
    pass   

def home(request):
    research = models.News.objects.filter(post_type = 'R').first()
    activities = models.Activity.objects
    activity = activities.first()
    volunteer = activities.filter(activity_type = 'V')
    community = models.Post.objects.first() #When Clubs get implemented change Post to ClubPosts (there would be some more changes too)
    return render(request,'alumniportal/main-body.html', {
        'page': 'home',
        'research':research,
        'activity': activity,
        'volunteer':volunteer,
        'community':community,
        })

def volunteer(request):
    volunteers = models.Activity.objects.filter(activity_type = 'V')
    return render(request, 'alumniportal/volunteer.html', {
        'page':'volunteer',
        'volunteers':volunteers,
        })

def activity(request):
    activities = models.Activity.objects.exclude(activity_type = 'V')
    return render(request,'alumniportal/activity.html', {
        'page': 'activity',
        'items':activities,
        'item_type':"ALL",
        })

def activity_items(request, item_type):
    for a in ACTIVITY_TYPE:
        if a[1]==item_type:
            activities = models.Activity.objects.filter(activity_type=a[0])
            return render(request, 'alumniportal/activity.html', {
                'page':'activity', 
                'items':activities,
                'item_type':item_type, 
                })
    return HttpResponseRedirect('/activity')

def community(request):
    return render(request,'alumniportal/communities.html', {'page': 'community'})

def news(request):
    admin_posts = models.News.objects
    news = admin_posts.all()[:2]
    achievements = admin_posts.filter(post_type = 'C')[:2]
    return render(request,'alumniportal/news.html', {
        'page': 'news',
        'news':news,
        'achievements':achievements,
        })

@login_required
def profile(request):
    try:
        profile = models.Profile.objects.get(user = request.user)
    except:
        return HttpResponseRedirect('/edit-profile')
    return render(request,'alumniportal/profile.html', {
        'page': 'profile',
        'profile':profile,
        })

@login_required
def view_profile(request, profile_id):
    profile = User.objects.get(username = profile_id).profile
    return render(request,'alumniportal/profile.html', {
        'page': 'profile',
        'profile':profile,
        })

def items(request, class_type, item_type):
    #####need to add continuously loading of news
    news = models.News.objects.all()
    print request.path
    # print POST_TYPE
    if class_type == "news":
        items = news
        for a in POST_TYPE:
            if a[1] == item_type:
                items = news.filter(post_type = a[0])

    ########WHat happens if none of the URL matches!!!!
    return render(request,'alumniportal/news-list.html', {
        'page': 'items',
        'items':items,
        'item_type':item_type,
        })

def createQuery(request, result, field):
    result = result | Q(**{field + "__icontains" : request.POST[field]})
    return result

@login_required
def search(request):
    profiles = []
    if request.POST:
        query = Q()
        # import pdb; pdb.set_trace()
        for field in request.POST:
            if field == "csrfmiddlewaretoken":
                continue
            if field == "name":
                list_of_words = request.POST['name'].split()
                for word in list_of_words:
                    query = query | Q(name__icontains = word)
                continue
            if request.POST[field]:
                query = createQuery(request, query, field)
                # query = query & Q(**field{field + "__icontains" : request.POST[field]})
                # list_of_words = request.POST['name']
            # for word in list_of_words:
                # profiles = profiles.filter(name__icontains=word)
        profiles = models.Profile.objects.filter(query)
        print query
        print profiles
    return render(request, 'alumniportal/search.html', {
        'page':"search", 
        'batches':PASS_OUT_YEARS,
        'majors':DEPARTMENTS,
        'profiles':profiles,
        })