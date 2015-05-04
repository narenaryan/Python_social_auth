
from django.shortcuts import render_to_response,redirect,render
from django.template.context import RequestContext
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User
from models import KIntegrate



def login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
    
        if not user:
            context = RequestContext(request,{'user': request.user , 'incorrect':1})
            return render_to_response('login.html',context_instance=context)
        
        context = RequestContext(request,{'user': request.user , 'incorrect':0})
        return render_to_response('home.html',context_instance=context)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
       context = RequestContext(request,{'user': request.user , 'incorrect':0})
       return render_to_response('login.html',context_instance=context)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        user = User.objects.create(username,email, password)
        context = RequestContext(request,{'user': request.user , 'incorrect':0})
        return render_to_response('home.html',context_instance=context)


    context = RequestContext(request,{'user': request.user , 'incorrect':0})
    return render_to_response('signup.html',context_instance=context)


def home(request):
    if request.method == 'POST':
        knowlarity_number = request.POST['knowlarity_number']
        app_url = request.POST['app_url']
        app_key = request.POST['api_key']
        integration_type = request.POST.get('integ')

        user = User.objects.get(username=request.user)

        KIntegrate.objects.create(user=user, number = knowlarity_number,integration_type = integration_type , app_url = app_url , app_key = app_key)

        return render(request,'home.html')

    users = User.objects.get(username=request.user)
    integrations = KIntegrate.objects.filter(user=request.user)
    print integrations
    return render(request,'home.html',{'integres':integrations})



def logout(request):
    auth_logout(request)
    return redirect('/')
