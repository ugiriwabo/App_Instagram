from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,UploadImageForm,CommentForm
from .models import Profile,Image,Comment


@login_required(login_url='/accounts/login/')
def welcome(request):
    img = Image.objects.all()
    search = Profile.objects.all()
    comments = Comment.objects.all()
    return render(request,'welcome.html',{"img": img,"comments":comments})

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

@login_required(login_url='/accounts/login/')
def search_results(request):
    current_user=request.user
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_images = Image.search_by_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def display_commentForm(request):
    current_user=request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('view_comment')

    else:
        form = CommentForm()
    return render(request, 'comment.html', {"form": form}) 

@login_required(login_url='/accounts/login/')
def view_comment(request):
    current_user=request.user
    comments=Comment.objects.filter(user=current_user.id) 
    return render(request,'my_comment.html',{'comments':comments})       