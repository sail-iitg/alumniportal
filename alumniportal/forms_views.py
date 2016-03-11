
from alumniportal import forms
from alumniportal import models
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files import File
from django.forms.models import modelformset_factory
from django.db import IntegrityError, transaction
from django.core.exceptions import ObjectDoesNotExist
######EDITED
import time, os

###maybe we can use different functions for each subcategory in profile later

####my edits
@login_required(login_url='/login/')
def add_activity(request):
    """
    display form to alumnus to add an Activity
    """
    if hasattr(request.user, 'profile'):
        profile = request.user.profile
    else:
        messages.error(request, "Create your Profile before adding activity")
        return HttpResponseRedirect('/edit-profile/')

    if request.method == "POST":
        form = forms.AddActivityForm(request.POST, request.FILES)
        form.fields['activity_type'].choices = [choice for choice in form.fields['activity_type'].choices if choice[0] != 'V']
        recent = models.Recent.objects.get_or_create(week = str(datetime.now().isocalendar()[1])+str(datetime.now().year))[0]
        # import pdb; pdb.set_trace()
        if form.is_valid():
            task = form.save(commit=False)
            image_list = request.FILES.getlist('files')
            task.profile = profile
            task.created = datetime.now()
            today = datetime.today().isocalendar()
            week = str(today[1])+str(today[0])
            tmp = models.Recent.objects.get_or_create(week=week)
            if tmp[1]:
                tmp[0].save()
            task.recent = tmp[0]
            task.save()

            for image in image_list:
                models.ActivityImage.objects.create(activity=task, image=image).save()
            messages.success(request, 'Activity Created')
    else:
        form = forms.AddActivityForm()
        # remove volunteering activity from activity type
        form.fields['activity_type'].choices = [choice for choice in form.fields['activity_type'].choices if choice[0] != 'V']
    return render(request, 'alumniportal/add-activity.html',
                  {'page': 'add-activity',
                   'form': form})

@login_required(login_url='/login/')
def add_volunteer(request):
    """
    display form to alumnus to add a Volunteering Activity
    """
    if hasattr(request.user, 'profile'):
        profile = request.user.profile
    else:
        messages.error(request, "Create your Profile before adding activity")
        return HttpResponseRedirect('/edit-profile/')

    if request.method == "POST":
        form = forms.AddActivityForm(request.POST, request.FILES)
        form.data[u'activity_type'] = u'V'
        recent = models.Recent.objects.get_or_create(week = str(datetime.now().isocalendar()[1])+str(datetime.now().year))[0]
        if form.is_valid():
            task = form.save(commit=False)
            image_list = request.FILES.getlist('files')
            task.profile = profile
            task.created = datetime.now()
            today = datetime.today().isocalendar()
            week = str(today[1])+str(today[0])
            tmp = models.Recent.objects.get_or_create(week=week)
            if tmp[1]:
                tmp[0].save()
            task.recent = tmp[0]
            task.save()

            for image in image_list:
                models.ActivityImage.objects.create(activity=task, image=image).save()
            messages.success(request, 'Volunteering Activity Created')
    else:
        form = forms.AddActivityForm()
        form.helper.form_action = '/volunteer/add/'
        # https://github.com/sail-iitg/alumniportal/issues/8
        del form.fields['activity_type']
    return render(request, 'alumniportal/add-activity.html',
                  {'page': 'add-activity',
                   'form': form,
                   'volunteer': True})

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

@login_required
def edit_iitg(request):
    try :
        profile = request.user.profile
    except ObjectDoesNotExist:
        print("profile doesn't exist")
        messages.error(request,'Please fill your personal details first.')
        return HttpResponseRedirect('/edit-profile/personal')
    if profile:
        formset = modelformset_factory(models.IITGExperience,exclude=('profile',),extra=1, can_delete=True )

        if request.method == "POST":
            _formset = formset(request.POST,request.FILES)
            if _formset.is_valid():
                instances = _formset.save(commit=False)
                for Experience in _formset:
                    if Experience.has_changed() and Experience.is_valid():
                        task = Experience.save(commit=False)
                        task.profile = profile
                        if Experience.changed_data == ['DELETE']:
                            task.delete()
                        else:
                            task.save()
                            messages.success(request,'Validated Data Saved.')
                return HttpResponseRedirect('/edit-profile/iitg')
        else :
            _formset = formset(queryset=models.IITGExperience.objects.filter(profile=profile).reverse())
        helper = forms.IITGExperienceFormSetHelper()
        return render(request,'alumniportal/edit-profile.html',{
            'formset':_formset,
            'page':'edit-profile',
            'profile':'iitg',
            'helper':helper,
            'username': request.user.username,
            'no_profile': not profile,
            })


    else :
        return HttpResponseRedirect('/')


@login_required
def edit_project(request):
    try :
        profile = request.user.profile
    except ObjectDoesNotExist:
        print("profile doesn't exist")
        messages.error(request,'Please fill your personal details first.')
        return HttpResponseRedirect('/edit-profile/personal')
    if profile:
        formset = modelformset_factory(models.Project,exclude=('profile','recent',),extra=1, can_delete=True  )
        if request.method == "POST":
            _formset = formset(request.POST,request.FILES)
            if _formset.is_valid():
                instances = _formset.save(commit=False)
                for Project in _formset:
                    if Project.has_changed() and Project.is_valid():
                        task = Project.save(commit=False)
                        if Project.changed_data == ['DELETE']:
                            task.delete()
                        else:
                            today = datetime.today().isocalendar()
                            week = str(today[1])+str(today[0])
                            tmp = models.Recent.objects.get_or_create(week=week)
                            if tmp[1]:
                                tmp[0].save()
                            task.recent = tmp[0]
                            task.profile = profile
                            task.save()
                            messages.success(request,'Validated Data Saved.')
                return HttpResponseRedirect('/edit-profile/project')
        else :
            _formset = formset(queryset=models.Project.objects.filter(profile=profile).reverse())
        helper = forms.ProjectFormSetHelper()
        return render(request,'alumniportal/edit-profile.html',{
            'formset':_formset,
            'page':'edit-profile',
            'profile':'project',
            'helper':helper,
            'username': request.user.username,
            'no_profile': not profile,
            })


    else :
        return HttpResponseRedirect('/')



@login_required
def edit_education(request):
    try :
        profile = request.user.profile
    except ObjectDoesNotExist:
        print("profile doesn't exist")
        messages.error(request,'Please fill your personal details first.')
        return HttpResponseRedirect('/edit-profile/personal')
    if profile:
        educations = models.Education.objects.filter(profile=profile)
        formset = modelformset_factory(models.Education,exclude=('profile',),extra=1, can_delete=True )
        
        if request.method == "POST":
            _formset = formset(request.POST,request.FILES)
        
            for Education in _formset:
                if Education.has_changed() and Education.is_valid():
                    task = Education.save(commit=False)
                    if Education.changed_data == ['DELETE']:
                        task.delete()
                    else:
                        task.profile = profile
                        task.save()
                        messages.success(request,'Validated Data Saved.')
            return HttpResponseRedirect('/edit-profile/education')

        
        else :
            _formset = formset(queryset=educations.reverse())
        
        helper = forms.EducationFormSetHelper()
        return render(request,'alumniportal/edit-profile.html',{
            'formset':_formset,
            'page':'edit-profile',
            'profile':'education',
            'helper':helper,
            'currents':educations,
            'current_education':profile.current_education,
            'username': request.user.username,
            'no_profile': not profile,
            })


    else :
        ##redirect to create profile - personal
        return HttpResponseRedirect('/')


@login_required
def edit_professional(request):
    try :
        profile = request.user.profile
    except ObjectDoesNotExist:
        print("profile doesn't exist")
        messages.error(request,'Please fill your personal details first.')
        return HttpResponseRedirect('/edit-profile/personal')
    if profile:
        formset = modelformset_factory(models.Job,exclude=('profile',),extra=1, can_delete=True  )
        jobs = models.Job.objects.filter(profile=profile)
        if request.method == "POST":
            _formset = formset(request.POST,request.FILES)
            for Job in _formset:
                if Job.has_changed() and Job.is_valid():
                    task = Job.save(commit=False)
                    if Job.changed_data == ['DELETE']:
                        Job.delete()
                    else:
                        task.profile = profile
                        task.save()
                        messages.success(request,'Data Saved.')
            return HttpResponseRedirect('/edit-profile/professional')
        else :
            _formset = formset(queryset=jobs.reverse())
        helper = forms.JobFormSetHelper()
        return render(request,'alumniportal/edit-profile.html',{
            'formset':_formset,
            'page':'edit-profile',
            'profile':'professional',
            'helper':helper,
            'currents':jobs,
            'current_job':profile.current_job,
            'username': request.user.username,
            'no_profile': not profile,
            })


    else :
        ##redirect to create profile - personal
        return HttpResponseRedirect('/')

@login_required
def edit_achievement(request):
    try :
        profile = request.user.profile
    except ObjectDoesNotExist:
        print("profile doesn't exist")
        messages.error(request,'Please fill your personal details first.')
        return HttpResponseRedirect('/edit-profile/personal')

    if profile:
        formset = modelformset_factory(models.Achievement,exclude=('profile','recent',),extra=1, can_delete=True  )
        if request.method == "POST":
            _formset = formset(request.POST,request.FILES)
            if _formset.is_valid():
                for Achievement in _formset:
                    if Achievement.has_changed() and Achievement.is_valid():
                        task = Achievement.save(commit=False)
                        if Achievement.changed_data == ['DELETE']:
                            Achievement.delete()
                        else:
                            today = datetime.today().isocalendar()
                            week = str(today[1])+str(today[0])
                            tmp = models.Recent.objects.get_or_create(week=week)
                            if tmp[1]:
                                tmp[0].save()
                            task.recent = tmp[0]
                            task.profile = profile
                            task.save()
                            messages.success(request,'Data Saved.')
                return HttpResponseRedirect('/edit-profile/achievement')
        else :
            _formset = formset(queryset=models.Achievement.objects.filter(profile=profile).reverse())
        helper = forms.AchievementFormSetHelper()
        return render(request,'alumniportal/edit-profile.html',{
            'formset':_formset,
            'page':'edit-profile',
            'profile':'achievement',
            'helper':helper,
            'username': request.user.username,
            'no_profile': not profile,
            })


    else :
        return HttpResponseRedirect('/')

@login_required
def edit_personal(request):
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
        # import pdb; pdb.set_trace()
        if form.is_valid():
            task = form.save(commit=False)
            task.last_edited = datetime.now()
            if not profile:
                task.user = request.user
            task.save()
            models.Blog.objects.create(profile=task)
            messages.success(request, 'Profile saved.')
    else:
        if profile:
            form = forms.EditProfileForm(instance=profile)
        else:
            form = forms.EditProfileForm()
    return render(request, 'alumniportal/edit-profile.html', {
        'page': 'edit-profile',
        'form': form,
        'profile':'personal',
        'username': request.user.username,
        'no_profile': not profile,
        })

def current(request):
    if request.POST:
        profile = request.user.profile
        if request.path == '/edit-profile/professional/current/':
            profile.current_job = models.Job.objects.get(id=request.POST['current'])
            profile.save()
            messages.success(request, "Changes Saved")
        elif request.path == '/edit-profile/education/current/':
            profile.current_education = models.Education.objects.get(id=request.POST['current'])
            profile.save()
            messages.success(request, "Changes Saved")
        else:
            messages.error(request, "Some invalid activity detected")
            return HttpResponseRedirect("/edit-profile")
    return HttpResponseRedirect("/edit-profile")

# @login_required(login_url='/login/')
# def edit_profile(request):
#     """
#     display form to alumnus for editing profile
#     """

#     # get user profile if exists
#     if hasattr(request.user, 'profile'):
#         profile = request.user.profile
#         IITGExperienceFormSet = modelformset_factory(forms.EditIITGExperienceForm)
#         IITGExperienceObjects = models.IITGExperience.objects.filter(profile=profile)
#         IITGExperienceData = [{'club_name': l.club_name, 'experience': l.experience} for l in IITGExperienceObjects]
#     else:
#         profile = None


#     if request.method == "POST" :
#         print(request.POST)
#         if request.POST.get("roll_no"):
#             if profile:

#                 PersonalForm = forms.EditProfileForm(request.POST, request.FILES, instance=profile)

#                     # print(request.POST.get('form'))
#                 # print(request.POST)
#                 # print(PersonalForm)
#             else:
#                 print("Profile DNE")
#                 PersonalForm = forms.EditProfileForm(request.POST, request.FILES)
#                 # print(PersonalForm)
#                 # print(PersonalForm)
#             if PersonalForm.is_valid():
#                 print("Validated")
#                 task = PersonalForm.save(commit=False)
#                 if not profile:
#                     task.user = request.user
#                     profile=request.user.profile
#                 task.save()
#                 messages.success(request, 'Profile saved.')

#                 print(type(task))
#                 ######add code to respond to request
#             else :
#                 messages.error(request, 'Please enter information in all required(*) fields. Personal')

#         elif request.POST.get("institute"):
#             print("r1")

#             if profile:
#                 try:
#                     education = models.Education.objects.get(profile=profile)
#                     EducationForm = forms.EditEducationForm(request.POST, request.FILES,instance=education)
#                 except models.Education.DoesNotExist:
#                     EducationForm = forms.EditEducationForm(request.POST, request.FILES)

#             else:
#                 print("Profile DNE")
#                 #####write code to ask them to fill personal form first and redirect them
#             # print(EducationForm.errors)
#             if EducationForm.is_valid():
#                 print("r3")
#                 print("Validated")
#                 task = EducationForm.save(commit=False)
#                 task.profile = profile
#                 task.save()
#                 messages.success(request, 'Education saved.')
#                 # print(type(task))
#             else :
#                 print("reached")
#                 messages.error(request, 'Please enter information in all required(*) fields.')



#         elif request.POST.get("experience"):
#             IITGExperience_formset = IITGExperienceFormSet(request.POST,request.FILES)

#             if not profile:
#                 print("Profile DNE")
#                 #####write code to ask them to fill personal form first and redirect them
#             if IITGExperience_formset.is_valid():

#                 new_IITGExperiences = []

#                 for IITGExperienceForm in IITGExperience_formset:
#                     task = IITGExperienceForm.save(commit=False)
#                     task.profile = profile
#                     task.save()
#                     print(type(task))
#                 messages.success(request, 'Experiences saved.')


#             else :
#                 print("reached")
#                 messages.error(request, 'Please enter information in all required(*) fields.')




#         elif request.POST.get("topic"):

#             if profile:
#                 try:
#                     project = models.Project.objects.get(profile=profile)
#                     ProjectForm = forms.EditProjectForm(request.POST, request.FILES,instance=project)
#                 except models.Project.DoesNotExist:
#                     ProjectForm = forms.EditProjectForm(request.POST, request.FILES)

#             else:
#                 print("Profile DNE")
#                 #####write code to ask them to fill personal form first and redirect them
#             print("reacheddd")
#             print(ProjectForm.errors)
#             if ProjectForm.is_valid():
#                 print("Validated")
#                 task = ProjectForm.save(commit=False)
#                 print(datetime.date)
#                 today = datetime.today()
#                 week_no = today.isocalendar()[1]
#                 year_no = today.isocalendar()[0]
#                 recent_week= str(models.Recent.objects.latest('week'))[:2]
#                 recent_year= str(models.Recent.objects.latest('week'))[-4:]

#                 if week_no == recent_week and year_no == recent_year :
#                     recent= models.Recent.objects.latest('week')
#                 else :
#                     recent = models.Recent(week=str(week_no)+str(year_no))
#                     recent.save()
#                 task.recent = models.Recent.objects.latest('week')
#                 task.profile = profile
#                 task.save()
#                 messages.success(request, 'Project Saved')
#             else :
#                 print("reached")
#                 messages.error(request, 'Please enter information in all required(*) fields.')

#         elif request.POST.get("achievement"):

#             if profile:
#                 try:
#                     achievement = models.Achievement.objects.get(profile=profile)
#                     AchievementForm = forms.EditAchievementForm(request.POST, request.FILES,instance=achievement)
#                 except models.Achievement.DoesNotExist:
#                     AchievementForm = forms.EditAchievementForm(request.POST, request.FILES)

#             else:
#                 print("Profile DNE")
#                 #####write code to ask them to fill personal form first and redirect them
#             print(AchievementForm.errors)
#             if AchievementForm.is_valid():
#                 print("Validated")
#                 task = AchievementForm.save(commit=False)
#                 print(datetime.date)
#                 today = datetime.today()
#                 week_no = today.isocalendar()[1]
#                 year_no = today.isocalendar()[0]
#                 recent_week= str(models.Recent.objects.latest('week'))[:2]
#                 recent_year= str(models.Recent.objects.latest('week'))[-4:]

#                 if week_no == recent_week and year_no == recent_year :
#                     recent= models.Recent.objects.latest('week')
#                 else :
#                     recent = models.Recent(week=str(week_no)+str(year_no))
#                     recent.save()
#                 task.recent = models.Recent.objects.latest('week')
#                 task.profile = profile
#                 task.save()
#                 messages.success(request, 'Achievement Saved')
#             else :
#                 print("reached")
#                 messages.error(request, 'Please enter information in all required(*) fields.')



#         elif request.POST.get("company"):

#             if profile:
#                 try:
#                     job = models.Job.objects.get(profile=profile)
#                     JobForm = forms.EditJobForm(request.POST, request.FILES,instance=job)
#                 except models.Job.DoesNotExist:
#                     JobForm = forms.EditJobForm(request.POST, request.FILES)

#             else:
#                 print("Profile DNE")
#                 #####write code to ask them to fill personal form first and redirect them
#             if JobForm.is_valid():
#                 print("Validated")
#                 task = JobForm.save(commit=False)
#                 task.profile = profile
#                 task.save()
#                 print(type(task))
#                 messages.success(request, 'Job saved.')
#             else :
#                 print("reached")
#                 messages.error(request, 'Please enter information in all required(*) fields.')



#     if profile:
#         PersonalForm = forms.EditProfileForm(instance=profile)
#         try:
#             education = models.Education.objects.get(profile=profile)
#             EducationForm = forms.EditEducationForm(instance=education)
#         except models.Education.DoesNotExist:
#             EducationForm = forms.EditEducationForm()

#         IITGExperience_formset = IITGExperienceFormSet(initial=IITGExperienceData)



#         # try:
#         #     iitgexp = models.IITGExperience.objects.get(profile=profile)
#         #     IITGExperienceForm = forms.EditIITGExperienceForm(instance=iitgexp)
#         # except models.IITGExperience.DoesNotExist:
#         #     IITGExperienceForm = forms.EditIITGExperienceForm()

#         try:
#             project = models.Project.objects.get(profile=profile)
#             ProjectForm = forms.EditProjectForm(instance=project)
#         except models.Project.DoesNotExist:
#             ProjectForm = forms.EditProjectForm()
#         try:
#             job = models.Job.objects.get(profile=profile)
#             JobForm = forms.EditJobForm(instance=job)
#         except models.Job.DoesNotExist:
#             JobForm = forms.EditJobForm()
#         try:
#             achievement = models.Achievement.objects.get(profile=profile)
#             AchievementForm = forms.EditAchievementForm(instance=job)
#         except models.Achievement.DoesNotExist:
#             AchievementForm = forms.EditAchievementForm()

#     else:
#         PersonalForm = forms.EditProfileForm()
#         EducationForm = forms.EditEducationForm()
#         IITGExperience_formset = IITGExperienceFormSet()
#         # IITGExperienceForm = forms.EditIITGExperienceForm()
#         ProjectForm = forms.EditProjectForm()
#         JobForm = forms.EditJobForm()
#         AchievementForm=forms.AchievementForm

#     return render(request, 'alumniportal/edit-profile.html',
#                   {'page': 'edit-profile',
#                    'PersonalForm': PersonalForm,
#                    'EducationForm':EducationForm,
#                    'IITGExperience_formset':IITGExperience_formset,
#                    'ProjectForm':ProjectForm,
#                    'JobForm':JobForm,
#                    'AchievementForm':AchievementForm,
#                    'username': request.user.username,
#                    'no_profile': not profile,
#                    })

#  # if models.Education.objects.get(profile=profile):
#  #                education = models.Education.objects.get(profile=profile)
#  #                EducationForm = forms.EditEducationForm(instance=education)
#  #            else :
#  #                EducationForm = forms.EditEducationForm()

@user_passes_test(lambda u: u.is_superuser)
def add_news(request):
    """
    Display form for adding news and redirect to published news
    """
    if request.method == 'POST':
        form = forms.AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save()
            return HttpResponseRedirect('/' + str(task.id) + '/news/')
    else:
        form = forms.AddNewsForm()
    return render(request, 'alumniportal/add-news.html',
                  {'page': 'add-news',
                   'form': form})


@user_passes_test(lambda u: u.is_superuser)
def edit_news(request, news_id):
    """
    Display form for editing news and redirect to published news
    """
    try:
        news = models.News.objects.get(id=news_id)
    except models.News.DoesNotExist:
        return HttpResponse('News (id: ' + str(news_id) + ') does not exist.')

    if request.method == 'POST':
        form = forms.AddNewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            task = form.save()
            return HttpResponseRedirect('/' + str(task.id) + '/news/')
    else:
        form = forms.AddNewsForm(instance=news)
        form.helper.form_action = '/' + str(news_id) + '/edit/news/'
        return render(request, 'alumniportal/add-news.html',
                  {'page': 'add-news',
                   'form': form,
                   'edit': True})


@login_required(login_url='/login/')
def add_post(request, username):
    """
    Display form for adding blog post and redirect to published post
    """
    if request.user.username != username:
        return HttpResponse('You do not have edit access to this blog')
    if request.method == 'POST':
        form = forms.AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.blog = request.user.profile.blog
            task.save()
            url = '/' + username + '/blog/' + str(task.id) + '/post/'
            return HttpResponseRedirect(url)
    else:
        form = forms.AddPostForm()
        form.helper.form_action = '/' + username + '/blog/add/post/'
    return render(request, 'alumniportal/add-post.html',
                  {'page': 'add-post',
                   'form': form})


@login_required(login_url='/login/')
def edit_post(request, username, post_id):
    """
    Display form for editing published blog post and redirect to published post
    """
    try:
        post = models.Post.objects.get(id=post_id)
    except models.Post.DoesNotExist:
        return HttpResponse('Post (id: ' + str(post_id) + ') does not exist.')
    if post.blog.profile.user != request.user or username != request.user.username:
        return HttpResponse('You do not have edit access to this post.')

    if request.method == 'POST':
        form = forms.AddPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            task = form.save()
            url = '/' + username + '/blog/' + str(task.id) + '/post/'
            return HttpResponseRedirect(url)
    else:
        form = forms.AddPostForm(instance=post)
        form.helper.form_action = '/' + username + '/blog/' + str(post_id) + '/edit/post/'
        return render(request, 'alumniportal/add-post.html',
                  {'page': 'add-post',
                   'form': form,
                   'edit': True})
