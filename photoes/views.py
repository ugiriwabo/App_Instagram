from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,ImageForm
from .models import Profile,Image


@login_required(login_url='/accounts/login/')
def welcome(request):
    img = Image.objects.all()
    return render(request,'welcome.html',{"img": img})

@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('welcome')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})