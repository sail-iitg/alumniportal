from django.shortcuts import render
from django.contrib import auth as authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if not request.user.is_authenticated():
        return render(request, 'login-page.html')
    else:
        return HttpResponseRedirect('/')

@login_required
def logout(request):
    """
    logs out user, only if he is already logged in.
    """
    authenticate.logout(request)
    return HttpResponseRedirect('/')

def auth(request):
    if request.POST:
        # next_url=''
        username = request.POST['username']
        password = request.POST['password']
        
        # next_url  = request.POST.get('next',False)
        # print(next_url)
        user = authenticate.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:  #is_active can be used to block a user
                authenticate.login(request, user)
                #logout(request)

            # if next_url != '' :
                # return HttpResponseRedirect(next_url)
            # else :
                # return HttpResponseRedirect('/')
        
    return HttpResponseRedirect('/')