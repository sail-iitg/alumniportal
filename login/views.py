from django.shortcuts import render
from django.contrib import auth as authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
#####edited
def login(request):
    next_url=None
    if request.GET:
        next_url  = request.GET.get('next',False)
    if not request.user.is_authenticated():
        if next_url is not None:
            return render(request, 'login-page.html',{'next':next_url})
        else :
            return render(request, 'login-page.html',{'next':''})

    else:
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
        
    return HttpResponseRedirect('/')