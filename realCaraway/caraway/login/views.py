from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login,authenticate

from .models import ParentCreation
from swingtime.models import EventType
from swingtime.forms import EventForm
from .forms import AdminCreationForm, ClassCreationForm, ParentCreationForm, User
from karate.urls import urlpatterns

#parent
#----------------------------------------------------------------------------------------
def SignUp(request):
    if request.method == 'POST':
        form = ParentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users/signup')
    else:
        form = ParentCreationForm()
        
    return render(request, 'signup.html', {'form': form})

#-------------------------------------------------------------------------------------------------
#admin
class SignUpAdmin(generic.CreateView):
    form_class = AdminCreationForm
    success_url = reverse_lazy('admin')
    template_name = 'signupAdmin.html'

#class-------------------------------------------------------------------------------------------
def SignUpClass(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClassCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # redirect to a new URL:
            classroom = request.POST.get('classroom','')
            classObj = EventType(label = classroom)
            classObj.save()

            return HttpResponseRedirect('/users/signup/class/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClassCreationForm()

    return render(request, 'signupClass.html', {'form': form})



@login_required
def Home(request):
    if request.user.is_superuser:
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect('/swingtime/karate/')

#--------------------------------------------------------------------------------------------------------