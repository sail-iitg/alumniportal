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

@login_required(login_url='/login/')
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
            form = forms.EditProfileForm(request.POST, request.FILES, instance=profile)
        else:
            form = forms.EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.last_edited = datetime.now()
            if not profile:
                task.user = request.user
            task.save()
            messages.success(request, 'Profile saved.')
    else:
        if profile:
            form = forms.EditProfileForm(instance=profile)
        else:
            form = forms.EditProfileForm()
    return render(request, 'alumniportal/edit-profile.html',
                  {'page': 'edit-profile',
                   'form': form})


####my edits
@login_required(login_url='/login/')
def add_activity(request):
    """
    display form to alumnus to add an Activity
    """
    if hasattr(request.user, 'profile'):
        profile = request.user.profile
    else:
        print("Create Profile before adding activity")
        return HttpResponseRedirect('/')

    if request.method == "POST":
        form = forms.AddActivityForm(request.POST, request.FILES)
        if form.is_valid():
            
            task = form.save(commit=False)
            #task.recent = models.Recent.objects.get(pk=1)
            #print(models.Recent.objects.get(pk=1).week)
            image_list = request.FILES.getlist('files')
            #####NOW GET DIRECTORY TO STORE IMAGES
            print(image_list)
            
            task.profile = profile
            task.created = datetime.now()
            ## RECENT
            timestamp = time.time() 
            today = datetime.date.today()
            week_no = today.isocalendar()[1]
            year_no = today.isocalendar()[0]
            recent_week= str(models.Recent.objects.latest('week'))[:2]
            recent_year= str(models.Recent.objects.latest('week'))[-4:]
            
            if week_no == recent_week and year_no == recent_year :
                recent= models.Recent.objects.latest('week')
            else :
                recent = models.Recent(week=str(week_no)+str(year_no))
                recent.save()
            task.recent = models.Recent.objects.latest('week')
            task.save()
            messages.success(request, 'Activity Created')
            recent.activities += "["+str(timestamp)+","+str(task.id)+"],"
    else:
        form = forms.AddActivityForm()
    return render(request, 'alumniportal/add-activity.html',
                  {'page': 'add-activity',
                   'form': form})

########NOT SHOWING UP IN ADMIN
# @login_required(login_url='/login/')
# def blog_details_edit(request):
#     """
#     display form to alumnus for editing profile
#     """

#     # get user profile if exists
#     if hasattr(request.user, 'profile'):
#         profile = request.user.profile
#     else:
#         print("Create Profile before adding blog")
#         return HttpResponseRedirect('/')

#     if request.method == "POST":
#         if profile:
#             form = forms.BlogDetailsEdit(request.POST, request.FILES, instance=profile)
#         else:
#             form = forms.BlogDetailsEdit(request.POST, request.FILES)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.profile = profile
#             image_list = request.FILES.getlist('images_field')
#             videos_list = request.FILES.getlist('videos_field')
#             #####NOW GET DIRECTORY TO STORE IMAGES
#             print(videos_list)
#             print(image_list)
#             print(task.profile.name)
#             task.save()
#             messages.success(request, 'Blog details updated.')
#     else:
#         if profile:
#             form = forms.BlogDetailsEdit(instance=profile)
#         else:
#             form = forms.BlogDetailsEdit()
#     return render(request, 'alumniportal/blog-details-edit.html',
#                   {'page': 'blog-details-edit',
#                    'form': form})


@login_required(login_url='/login/')
def blog_details_edit(request):
    """
    display form to alumnus for editing blog details
    """
    if hasattr(request.user.profile, 'blog'):
        blog = request.user.profile.blog
        # print(blog.about_me)
    else:
        blog= None
    # get user profile if exists
    if hasattr(request.user, 'profile'):
        profile = request.user.profile
    else:
        print("Create Profile before adding blog")
        return HttpResponseRedirect('/')


    if request.method == "POST":
        if blog:
            form = forms.BlogDetailsEdit(request.POST, request.FILES, instance=blog)
        else:
            form = forms.BlogDetailsEdit(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.profile = profile
            task.save()
            messages.success(request, 'Blog details saved.')
    else:
        if blog:
            form = forms.BlogDetailsEdit(instance=blog)
        else:
            form = forms.BlogDetailsEdit()
    return render(request, 'alumniportal/blog-details-edit.html',
                  {'page': 'blog-details-edit',
                   'form': form})

