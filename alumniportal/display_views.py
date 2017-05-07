#####DO NOT CLOSE WINDOW
from alumniportal import forms
from alumniportal import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import time
import json
from datetime import datetime
from constants import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

####To pass the required recent objects in required numbers
def get_recent_objects():
    pass

def has_blog(user):
    return hasattr(user, 'profile') and hasattr(user.profile, 'blog')

def home(request):
    news = models.News.objects
    research = news.filter(post_type = 'R').first()
    activities = models.Activity.objects
    activity = activities.filter(status='Accepted').first()
    achievement = news.filter(post_type = 'C').first()
    volunteer = activities.filter(status='Accepted').filter(activity_type = 'V').first()
    pending_count = None
    if request.user.is_superuser:
        pending_count = len(activities.filter(status='Pending'))
    #When Clubs get implemented change Post to ClubPosts (there would be some more changes too)
    community = models.Post.objects.first() 
    return render(request,'alumniportal/main-body.html', {
        'page': 'home',
        'research':research,
        'activity': activity,
        'pending_count':pending_count,
        'achievement':achievement,
        'volunteer':volunteer,
        'community':community,
        'rolling_news':list(news.all())[-3:],
        })

def volunteer(request):
    return items(request, "activity", "Volunteering")

def activity(request):
    return items(request, "activity", "All")

def news(request):
    return items(request, "news", "All")

main_groups = ['Technical Board', 'Sports Board', 'Cultural Board']
def community(request):
    club_posts = {}
    for grp in main_groups:
        club, create = models.Club.objects.get_or_create(name = grp, description = "Aim to spread awareness about the happenings in the campus from the side of " + grp, group_type = 'O')
        club_posts[grp] = models.ClubPost.objects.filter(club = club)[:1]
    blog_posts = models.Post.objects.all()[:5]
    # print club_posts
    return render(request,'alumniportal/communities.html', {
        'page': 'community',
        'rolling_news':list(models.News.objects.all())[-3:],
        'club_posts': club_posts,
        'blog_posts': blog_posts,
        'add_right' : request.user.is_superuser,
        })


@login_required(login_url='/login/')
def change_password(request):
    return render(request, 'alumniportal/widgets/change-password.html', {
        'page':'change-password',
        })

@login_required(login_url='/login/')
def profile(request):
    try:
        profile = models.Profile.objects.get(user = request.user)
    except:
        messages.error(request, "Please create your profile.")
        return HttpResponseRedirect('/edit-profile')
    # import pdb; pdb.set_trace()
    return render(request,'alumniportal/profile.html', {
        'page': 'profile',
        'rolling_news':list(models.News.objects.all())[-3:],
        'profile':profile,
        'is_self_profile': True,
        })

@login_required(login_url='/login/')
def view_profile(request, profile_id):
    profile = User.objects.get(username = profile_id).profile
    return render(request,'alumniportal/profile.html', {
        'page': 'profile',
        'rolling_news':list(models.News.objects.all())[-3:],
        'profile':profile,
        'is_self_profile': False,
        })

def items(request, class_type, item_type):
    #####need to add continuously loading of news
    items = None
    # print "In items function"
    add_right = False
    if class_type == "news":
        news = models.News.objects.all()
        items = news
        add_right = request.user.is_superuser
        # import pdb; pdb.set_trace()
        for a in POST_TYPE:
            print items
            if a[1] == item_type:
                items = news.filter(post_type = a[0])
    elif class_type == "activity":
        activities = models.Activity.objects.filter(status='Accepted')
        items = activities
        if hasattr(request.user, 'profile') and hasattr(request.user.profile, 'blog'):
            add_right = True
        for a in ACTIVITY_TYPE:
            print items
            if a[1] == item_type:
                items = activities.filter(status='Accepted').filter(activity_type = a[0])

    paginator = Paginator(items, 10)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
        
    # print request.path
    pending_count = None
    if request.user.is_superuser:
        pending_count = len(models.Activity.objects.filter(status='Pending'))

    ########WHat happens if none of the URL matches!!!!
    return render(request,'alumniportal/items.html', {
        'page': 'items',
        'items':items,
        'item_type':item_type,
        'class_type' : class_type,
        'pending_count': pending_count,
        'file': class_type + ".html",
        'rolling_news':list(models.News.objects.all())[-3:],
        'add_right': add_right,
        })

# ignoreField = ['company']
# @login_required
def createQuery(queryset, result, field):
    # import pdb; pdb.set_trace()
    print queryset, result,field
    result = result | Q(**{field + "__icontains" : queryset[field]})
    return result

@login_required(login_url='/login/')
def search(request):
    profiles = []
    print request.POST
    print request.GET
    print request.path

    if request.POST or request.GET:
        query = Q()
        queryset = request.POST.copy()

        page = request.POST.get('page')
        past_company = queryset['company']
        past_education = queryset['institute']
        if queryset['name']:
            list_of_words = queryset['name'].split()
            for word in list_of_words:
                query = query | Q(name__icontains = word)
        del queryset['page']
        del queryset['company']
        del queryset['csrfmiddlewaretoken']
        del queryset['institute']
        del queryset['name']
        
        for field in queryset:
            if queryset[field]:
                query = createQuery(queryset, query, field)
        if past_company:
            query = query | Q(jobs__company__icontains = past_company)
        if past_education:
            query = query | Q(educations__institute__icontains = past_education)

        profiles = models.Profile.objects.filter(query).distinct()
        print query
        print profiles

        paginator = Paginator(profiles, 20)
        try:
            profiles = paginator.page(page)
        except PageNotAnInteger:
            profiles = paginator.page(1)
        except EmptyPage:
            profiles = paginator.page(paginator.num_pages)

        # return HttpResponse(profiles)
    return render(request, 'alumniportal/search.html', {
        'page':"search",
        'batches':PASS_OUT_YEARS,
        'majors':DEPARTMENTS,
        'hostels':HOSTELS,
        'profiles':profiles,
        'rolling_news':list(models.News.objects.all())[-3:],
        })

@user_passes_test(has_blog, login_url = '/edit-profile/')
@login_required(login_url='/login/')
def detail(request, class_type, id):
    edit_right = False
    if class_type == 'news':
        edit_right = request.user.is_superuser
        try:
            item = models.News.objects.get(id=id)
        except ObjectDoesNotExist:
            raise Http404("404 Not Found")
    elif class_type == 'activity':
        try:
            item = models.Activity.objects.get(id=id)
            edit_right = (item.profile.user == request.user)
            if (request.user.is_superuser) or (edit_right):
                pass
            elif item.status == 'Pending' or item.status == 'Denied':
                raise Http404("404 Not Found")
        except ObjectDoesNotExist:
            raise Http404("404 Not Found")
        print "In actvity"
    elif class_type == 'community':
        try:
            item = models.ClubPost.objects.get(id=id)
            if (item.club.group_type == 'X' and not request.user.is_authenticated()):
                messages.error("Please login to see this page")
                return HttpResponseRedirect('/login/')

            edit_right = (item.member.user == request.user)
        except ObjectDoesNotExist:
            raise Http404("404 Not Found")
    return render(request, 'alumniportal/detail.html', {
        'item' : item,
        'page' : 'detail',
        'class_type' : class_type,
        'status':STATUS,
        'edit_right' : edit_right,
        })

@login_required(login_url='/login/')
def post_detail(request, username, post_id):
    item = models.Post.objects.get(id=post_id)
    if item.blog.profile.user.username != username:
        return HttpResponse('User post mismatch error. Please report to'
                            'administrator if this error persists.')
    return render(request, 'alumniportal/detail.html', {
        'page': 'detail',
        'item': item,
        'class_type': "blog",
        'edit_right': (item.blog.profile.user == request.user),
        'all_comments': item.postcomment_set.all(),
        'comment_form': forms.PostCommentForm(),
        'user_has_profile': hasattr(request.user, 'profile'),
        })

@login_required(login_url='/login/')
def blog(request, username = None):
    if not username:
        username = request.user.username
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse('Username does not exist.')
    blog = user.profile.blog
    posts = blog.post_set.all()
    return render(request,'alumniportal/blog.html', {
        'page': 'items',
        'posts': posts,
        'is_editor': (blog.profile.user == request.user),
        'rolling_news':list(models.News.objects.all())[-3:],
        'username': user.username,
        })

@user_passes_test(lambda u: u.is_superuser)
def approval(request, id = None):
    activities = models.Activity.objects.filter(status = 'Pending')
    if request.POST:
        item = models.Activity.objects.get(id=id)
        item.status = request.POST['status']
        item.save()
        return HttpResponseRedirect('/approval')
    return render(request, 'alumniportal/items.html', {
        'file': "activity.html",
        'items':activities,
        'status':STATUS,
        'page': 'items',
        'item_type':"all",
        'class_type' : "activity",
        'rolling_news':list(models.News.objects.all())[-3:],
        'add_right': False,
        })