from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,UploadImageForm
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
        return redirect('view_profile')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def view_profile(request):
    current_user=request.user
    profile=Profile.objects.get(user=current_user.id) 
    images=Profile.get_profile(profile.user_id)

    return render(request,'my_profile.html',{'profile':profile,'images':images})


@login_required(login_url='/accounts/login/')
def upload_image(request):
    current_user=request.user
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('welcome')

    else:
        form = UploadImageForm()
    return render(request, 'image.html', {"form": form})