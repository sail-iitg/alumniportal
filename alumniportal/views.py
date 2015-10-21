from alumniportal import forms
from alumniportal import models
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

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

def edit_profile(request):
    """
    display form to alumnus for editing profile
    """

    # get user profile if exists
    if hasattr(request.user, 'profile'):
        profile = request.user.profile
    else:
        profile = None

    if request.method == "POST":
        if profile:
            form = forms.EditProfileForm(request.POST, request.FILES,
                                     instance=profile)
        else:
            form = forms.EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.last_edited = datetime.now()
            if not profile:
                task.user = request.user
            task.save()
            messages.success(request,
                'Profile saved.')
    else:
        if profile:
            form = forms.EditProfileForm(instance=profile)
        else:
            form = forms.EditProfileForm()
    return render(request, 'alumniportal/edit-profile.html',
                  {'page': 'edit-profile',
                   'form': form})
