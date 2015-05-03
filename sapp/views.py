
from django.shortcuts import render_to_response,redirect
from django.template.context import RequestContext
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.http import HttpResponse



def home(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        print user
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if not user:
        	data = {}
        	return HttpResponse(data, content_type='application/json')
        else:
        	return render_to_response(request,'home.html',{'incorrect':0})

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
       context = RequestContext(request,{'user': request.user , 'incorrect':0})
       return render_to_response('home.html',context_instance=context)


def logout(request):
    auth_logout(request)
    return redirect('/home')
