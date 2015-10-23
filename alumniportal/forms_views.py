#####DO NOT CLOSE WINDOW
from alumniportal import forms
from alumniportal import models
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
######EDITED
import time




###maybe we can use different functions for each subcategory in profile
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

    if request.method == "POST" :
        print(request.POST)
        if request.POST.get("roll_no"):
            if profile:
                
                PersonalForm = forms.EditProfileForm(request.POST, request.FILES, instance=profile)

                    # print(request.POST.get('form'))
                # print(request.POST)
                # print(PersonalForm)
            else:
                print("Profile DNE")
                PersonalForm = forms.EditProfileForm(request.POST, request.FILES)
                # print(PersonalForm)
                # print(PersonalForm)
            if PersonalForm.is_valid():
                print("Validated")
                task = PersonalForm.save(commit=False)
                if not profile:
                    task.user = request.user
                    profile=request.user.profile
                task.save()
                messages.success(request, 'Profile saved.')

                print(type(task))
                ######add code to respond to request
            else :
                messages.error(request, 'Please enter information in all required(*) fields. Personal')

        elif request.POST.get("institute"):
            print("r1")

            if profile:
                try:
                    education = models.Education.objects.get(profile=profile)
                    EducationForm = forms.EditEducationForm(request.POST, request.FILES,instance=education)
                except models.Education.DoesNotExist:
                    EducationForm = forms.EditEducationForm(request.POST, request.FILES)

            else:
                print("Profile DNE")
                #####write code to ask them to fill personal form first and redirect them
            # print(EducationForm.errors)
            if EducationForm.is_valid():
                print("r3")
                print("Validated")
                task = EducationForm.save(commit=False)
                task.profile = profile
                task.save()
                messages.success(request, 'Education saved.')
                # print(type(task))
            else :
                print("reached")
                messages.error(request, 'Please enter information in all required(*) fields.')
                

        
        elif request.POST.get("experience"):

            if profile:
                try:
                    iitgexp = models.IITGExperience.objects.get(profile=profile)
                    IITGExperienceForm = forms.EditIITGExperienceForm(request.POST, request.FILES,instance=iitgexp)
                except models.IITGExperience.DoesNotExist:
                    IITGExperienceForm = forms.EditIITGExperienceForm(request.POST, request.FILES)

            else:
                print("Profile DNE")
                #####write code to ask them to fill personal form first and redirect them
            if IITGExperienceForm.is_valid():
                print("Validated")
                task = IITGExperienceForm.save(commit=False)
                task.profile = profile
                task.save()
                print(type(task))
                messages.success(request, 'Experiences saved.')
            else :
                print("reached")
                messages.error(request, 'Please enter information in all required(*) fields.')
        
        elif request.POST.get("topic"):

            if profile:
                try:
                    project = models.Project.objects.get(profile=profile)
                    ProjectForm = forms.EditProjectForm(request.POST, request.FILES,instance=project)
                except models.Project.DoesNotExist:
                    ProjectForm = forms.EditProjectForm(request.POST, request.FILES)

            else:
                print("Profile DNE")
                #####write code to ask them to fill personal form first and redirect them
            print("reacheddd")
            print(ProjectForm.errors)
            if ProjectForm.is_valid():
                print("Validated")
                task = ProjectForm.save(commit=False)
                print(datetime.date)
                today = datetime.today()
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
                task.profile = profile
                task.save()
                messages.success(request, 'Project Saved')
            else :
                print("reached")
                messages.error(request, 'Please enter information in all required(*) fields.')

        elif request.POST.get("achievement"):

            if profile:
                try:
                    achievement = models.Achievement.objects.get(profile=profile)
                    AchievementForm = forms.EditAchievementForm(request.POST, request.FILES,instance=achievement)
                except models.Achievement.DoesNotExist:
                    AchievementForm = forms.EditAchievementForm(request.POST, request.FILES)

            else:
                print("Profile DNE")
                #####write code to ask them to fill personal form first and redirect them
            print(AchievementForm.errors)
            if AchievementForm.is_valid():
                print("Validated")
                task = AchievementForm.save(commit=False)
                print(datetime.date)
                today = datetime.today()
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
                task.profile = profile
                task.save()
                messages.success(request, 'Achievement Saved')
            else :
                print("reached")
                messages.error(request, 'Please enter information in all required(*) fields.')



        elif request.POST.get("company"):

            if profile:
                try:
                    job = models.Job.objects.get(profile=profile)
                    JobForm = forms.EditJobForm(request.POST, request.FILES,instance=job)
                except models.Job.DoesNotExist:
                    JobForm = forms.EditJobForm(request.POST, request.FILES)

            else:
                print("Profile DNE")
                #####write code to ask them to fill personal form first and redirect them
            if JobForm.is_valid():
                print("Validated")
                task = JobForm.save(commit=False)
                task.profile = profile
                task.save()
                print(type(task))
                messages.success(request, 'Job saved.')
            else :
                print("reached")
                messages.error(request, 'Please enter information in all required(*) fields.')


            
    if profile:
        PersonalForm = forms.EditProfileForm(instance=profile)
        try:
            education = models.Education.objects.get(profile=profile)
            EducationForm = forms.EditEducationForm(instance=education)
        except models.Education.DoesNotExist:
            EducationForm = forms.EditEducationForm()
        try:
            iitgexp = models.IITGExperience.objects.get(profile=profile)
            IITGExperienceForm = forms.EditIITGExperienceForm(instance=iitgexp)
        except models.IITGExperience.DoesNotExist:
            IITGExperienceForm = forms.EditIITGExperienceForm()
        try:
            project = models.Project.objects.get(profile=profile)
            ProjectForm = forms.EditProjectForm(instance=project)
        except models.Project.DoesNotExist:
            ProjectForm = forms.EditProjectForm()
        try:
            job = models.Job.objects.get(profile=profile)
            JobForm = forms.EditJobForm(instance=job)
        except models.Job.DoesNotExist:
            JobForm = forms.EditJobForm()
        try:
            achievement = models.Achievement.objects.get(profile=profile)
            AchievementForm = forms.EditAchievementForm(instance=job)
        except models.Achievement.DoesNotExist:
            AchievementForm = forms.EditAchievementForm()

    else:
        PersonalForm = forms.EditProfileForm()
        EducationForm = forms.EditEducationForm()
        IITGExperienceForm = forms.EditIITGExperienceForm()
        ProjectForm = forms.EditProjectForm()
        JobForm = forms.EditJobForm()
        AchievementForm=forms.AchievementForm
    print(PersonalForm)    
    return render(request, 'alumniportal/edit-profile.html',
                  {'page': 'edit-profile',
                   'PersonalForm': PersonalForm,
                   'EducationForm':EducationForm,
                   'IITGExperienceForm':IITGExperienceForm,
                   'ProjectForm':ProjectForm,
                   'JobForm':JobForm,
                   'AchievementForm':AchievementForm,
                   })

 # if models.Education.objects.get(profile=profile):
 #                education = models.Education.objects.get(profile=profile)
 #                EducationForm = forms.EditEducationForm(instance=education)
 #            else :
 #                EducationForm = forms.EditEducationForm()

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
            today = datetime.today()
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

