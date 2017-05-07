
from alumniportal import forms
from alumniportal import models
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.conf import settings
from django.core.files import File
from django.forms.models import modelformset_factory
from django.db import IntegrityError, transaction
from django.core.exceptions import ObjectDoesNotExist
import time, os
import json

def has_blog(user):
    return hasattr(user, 'profile') and hasattr(user.profile, 'blog')

@user_passes_test(has_blog, login_url = '/edit-profile/')
@login_required(login_url='/login/')
def add_activity(request):
    """
    display form to alumnus to add an Activity
    """
    profile = request.user.profile

    if request.method == "POST":
        form = forms.AddActivityForm(request.POST, request.FILES)
        form.fields['activity_type'].choices = [choice for choice in form.fields['activity_type'].choices if choice[0] != 'V']
        recent, created = models.Recent.objects.get_or_create(week = str(datetime.now().isocalendar()[1])+str(datetime.now().year))
        # import pdb; pdb.set_trace()
        if form.is_valid():
            task = form.save(commit=False)
            image_list = request.FILES.getlist('files')
            task.profile = profile
            task.created = datetime.now()
            task.status = 'Pending'
            if created:
                recent.save()
            task.recent = recent
            task.save()

            for image in image_list:
                models.ActivityImage.objects.create(activity=task, image=image).save()
            return HttpResponseRedirect('/activity/' + str(task.id))
        else:
            messages.error(request, 'Fill the required fields.')
    else:
        form = forms.AddActivityForm()
        # remove volunteering activity from activity type
        form.fields['activity_type'].choices = [choice for choice in form.fields['activity_type'].choices if choice[0] != 'V']
    return render(request, 'alumniportal/add-activity.html', {
        'page': 'add-activity',
        'form': form,
        })

@user_passes_test(lambda u: u.is_superuser)
def add_news(request):
    """
    Display form for adding news and redirect to published news
    """
    if request.method == 'POST':
        form = forms.AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save()
            return HttpResponseRedirect('/news/' + str(task.id))
    else:
        form = forms.AddNewsForm()
    return render(request, 'alumniportal/add-edit.html',{
        'page': 'add',
        'class_type' : 'news',
        'form': form,
        'edit_right' : False,
        })

@user_passes_test(lambda u: u.is_superuser)
def add_community(request):
    if request.method == 'POST':
        form = forms.AddClubPostForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.member = request.user.profile
            task.timestamp = datetime.now()
            task.save()
            return HttpResponseRedirect('/community/' + str(task.id))
    else:
        form = forms.AddClubPostForm()
    return render(request, 'alumniportal/add-edit.html',{
        'page': 'add',
        'class_type' : 'Club Post',
        'form': form,
        'edit_right' : False,
        })    


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

@user_passes_test(has_blog, login_url = '/edit-profile/')
@login_required(login_url='/login/')
def add_volunteer(request):
    """
    display form to alumnus to add a Volunteering Activity
    """
    profile = request.user.profile

    if request.method == "POST":
        form = forms.AddActivityForm(request.POST, request.FILES)
        form.data[u'activity_type'] = u'V'
        recent, created = models.Recent.objects.get_or_create(week = str(datetime.now().isocalendar()[1])+str(datetime.now().year))[0]
        if form.is_valid():
            task = form.save(commit=False)
            image_list = request.FILES.getlist('files')
            task.profile = profile
            task.created = datetime.now()
            if created:
                recent.save()
            task.recent = recent
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

@user_passes_test(has_blog, login_url = '/edit-profile/')
@login_required
def edit_blog_details(request):
    # get user profile if exists
    blog = request.user.profile.blog
    profile = request.user.profile

    if request.method == "POST":
        if blog:
            form = forms.EditBlogDetails(request.POST, request.FILES, instance=blog)
        else:
            form = forms.EditBlogDetails(request.POST, request.FILES)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            task = form.save(commit=False)
            task.profile = profile
            task.save()
            messages.success(request, 'Blog details saved.')
    else:
        if blog:
            form = forms.EditBlogDetails(instance=blog)
        else:
            form = forms.EditBlogDetails()
    return render(request, 'alumniportal/edit-profile.html', {
        'page': 'edit-profile',
        'form': form,
        'profile':'blog',
        'username': request.user.username,
        'no_profile': not profile,
        })

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
                    if Experience.has_changed():
                        if Experience.is_valid():
                            task = Experience.save(commit=False)
                            task.profile = profile
                            if Experience.changed_data == ['DELETE']:
                                task.delete()
                            else:
                                task.save()
                                messages.success(request, 'Validated Data Saved.')
                        else:
                            messages.error(request, 'Please enter all necessary fields')
                    else:
                        messages.success(request, 'No changes made.')
                return HttpResponseRedirect('/edit-profile/iitg')
            else:
                messages.error(request, 'Please enter all necessary fields')
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
                    elif Project.has_changed() :
                        messages.error(request,'Please enter all necessary fields')
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
                elif Education.has_changed() :
                    messages.error(request,'Please enter all necessary fields')
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
            'currentEducation':profile.currentEducation,
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
                elif Job.has_changed() :
                    messages.error(request,'Please enter all necessary fields')
                    print messages
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
            'currentJob':profile.currentJob,
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
                    elif Achievement.has_changed() :
                        messages.error(request,'Please enter all necessary fields')
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
                models.Blog.objects.create(profile=task).save()
            if profile:
                if not hasattr(request.user.profile, 'blog'):
                    models.Blog.objects.create(profile=task).save()
            task.save()
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
            profile.currentJob = models.Job.objects.get(id=request.POST['current'])
            profile.save()
            messages.success(request, "Changes Saved")
        elif request.path == '/edit-profile/education/current/':
            profile.currentEducation = models.Education.objects.get(id=request.POST['current'])
            profile.save()
            messages.success(request, "Changes Saved")
        else:
            messages.error(request, "Some invalid activity detected")
            return HttpResponseRedirect("/edit-profile")
    return HttpResponseRedirect("/edit-profile")



def can_edit(request, item, class_type):
    if class_type == 'news':
        return request.user.is_superuser
    elif class_type == 'activity':
        return (item.profile.user == request.user)
    elif class_type == 'community':
        return (item.member.user == request.user)

# @user_passes_test(lambda u: u.is_superuser)
class_form_fn = {'news': forms.AddNewsForm, 'activity': forms.AddActivityForm, 'community': forms.AddClubPostForm}
def edit(request, class_type, id):
    """
    Display form for editing news and redirect to published news
    """
    try:
        item = models.class_model_fn[class_type].objects.get(id=id)
    except models.class_model_fn[class_type].DoesNotExist:
        return HttpResponse('Does not exist.')

    edit_right = can_edit(request, item, class_type)
    if edit_right:
        print "Edit right True"
        if request.method == 'POST':
            form = class_form_fn[class_type](request.POST, request.FILES, instance=item)
            # import pdb; pdb.set_trace()
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/' + class_type + '/' + str(item.id))
            else :
                form.helper.form_action = '/' + class_type + '/' + str(item.id) + '/edit/'
                messages.error(request,'Please enter all necessary fields correctly.')
        else:
            form = class_form_fn[class_type](instance=item)
        form.helper.form_action = '/' + class_type + '/' + str(item.id) + '/edit/'
    else:
        print "Edit right False"
        messages.error(request, 'Sorry! You do not have the permission to edit the requested form.')
        return HttpResponseRedirect('/' + class_type + '/')
    return render(request, 'alumniportal/add-edit.html', {
            'page': 'add',
            'form': form,
            'edit_right': edit_right,
            'class_type': class_type,
        })

def delete(request, class_type, id):
    """
    Display form for editing news and redirect to published news
    """
    try:
        item = models.class_model_fn[class_type].objects.get(id=id)
    except models.class_model_fn[class_type].DoesNotExist:
        return HttpResponse('Does not exist.')

    edit_right = can_edit(request, item, class_type)
    if edit_right:
        item.delete()
        messages.success(request,'The content has been deleted')
        return HttpResponseRedirect('/' + class_type + '/')
    else:
        print "Edit right False"
        messages.error(request, 'Sorry! You do not have the permission to delete this content.')
        return HttpResponseRedirect('/' + class_type + '/')
    return render(request, 'alumniportal/add-edit.html', {
            'page': 'add',
            'form': form,
            'edit_right': edit_right,
            'class_type': class_type,
        })

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
            url = '/' + username + '/blog/post/' + str(task.id)
            return HttpResponseRedirect(url)
        else:
            messages.error(request,'Please enter all necessary fields correctly')
    else:
        form = forms.AddPostForm(instance=post)
    form.helper.form_action = '#'
    return render(request, 'alumniportal/add-post.html',
              {'page': 'add-post',
               'form': form,
               'edit': True})


@login_required(login_url='/login/')
def add_post_comment(request, username, post_id):
    """
    Process form for adding blog post comments
    """
    try:
        post = models.Post.objects.get(id=post_id)
    except models.Post.DoesNotExist:
        return HttpResponse('Post (id: ' + str(post_id) + ') does not exist.')
    if request.method == 'POST':
        comment = request.POST.get('comment')
        response_data = {}
        if not hasattr(request.user, 'profile'):
            return HttpResponse('Fill your profile to comment.')

        post_comment = models.PostComment(comment=comment, post=post,
                                          author=request.user.profile)
        post_comment.save()

        response_data['result'] = 'Create post successful!'
        response_data['comment_pk'] = post_comment.pk
        response_data['comment_text'] = post_comment.comment
        response_data['post_pk'] = post_comment.post.pk

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        raise Http404('Page not found')


@login_required(login_url='/login/')
def post_comments_list(request, username, post_id):
    """
    Return required post comments as json object
    """
    try:
        post = models.Post.objects.get(id=post_id)
    except models.Post.DoesNotExist:
        return HttpResponse('Post (id: ' + str(post_id) + ') does not exist.')
    if request.method == 'POST':
        comments = post.postcomment_set.all()
        comment_ids = [str(cns.id) for cns in comments]
        comment_authors = [cns.author.name for cns in comments]
        comment_texts = [cns.comment for cns in comments]

        response_data = {
            'comment_ids': comment_ids,
            'comment_authors': comment_authors,
            'comment_texts': comment_texts,
        }

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        raise Http404('Page not found')
