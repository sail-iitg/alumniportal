from django.shortcuts import render
from django.contrib import auth as authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User

def login(request):
    next_url=None
    if request.GET:
        next_url  = request.GET.get('next',False)
    if not request.user.is_authenticated():
        if next_url is not None:
            return render(request, 'login-page.html',{'next':next_url,'page':'login'})
        else :
            return render(request, 'login-page.html',{'next':'','page':'login'})
    else:
        return HttpResponseRedirect('/')

@login_required
def change_password(request):
    """
    Authenticates user from the username and password from POST
    """
    username = request.user.username
    password = request.POST.get('password', '')
    user = authenticate.authenticate(username=username, password=password)

    if user is not None and request.POST['password1'] == request.POST['password2']:
        u = User.objects.get(username=username)
        u.set_password(request.POST['password1'])
        u.save()
        print "changed"
        messages.success(request, "Password Changed successfully. Login again!")
        return HttpResponseRedirect('/profile/change-password/')
        # render(request, 'Permission/login.html', {
        #     'success':True,
        #     'message2':"Password changed successfully",
        #     })
    elif user is not None:
        print "do not match"
        messages.error(request, "New password do not match!")
        return HttpResponseRedirect('/profile/change-password/')
        # return render(request, 'Permission/login.html', {
        #     'success':False,
        #     'message2':"New Passwords didn't match",
        #     })
    else:
        print "incorrects"
        messages.error(request, "Incorrect Old Password")
        return HttpResponseRedirect('/profile/change-password/')
        # return render(request, 'Permission/login.html', {
        #     'success':False,
        #     'message2':"Username or Password is incorrect"
        #     })
    return HttpResponseRedirect('/')


@login_required
def logout(request):
    """
    logs out user, only if he is already logged in.
    """
    authenticate.logout(request)
    return HttpResponseRedirect('/')

##### edited
def auth(request):
    if request.POST:
        next_url=''
        username = request.POST['username']
        password = request.POST['password']
        
        next_url  = request.POST.get('next',False)
        user = authenticate.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:  #is_active can be used to block a user
                authenticate.login(request, user)
            if next_url != '' :
                return HttpResponseRedirect(next_url)
            else :
                return HttpResponseRedirect('/')
        else:
            messages.error(request, "Incorrect Username or Password!")
    return HttpResponseRedirect('/')