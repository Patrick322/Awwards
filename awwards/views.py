from django.shortcuts import render,redirect
from .models import *
from .forms import ProjectUpload,ProfileForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets


def home(request):
    projects = Post.objects.all()
    return render(request, 'projects/index.html',{"projects":projects})

@login_required (login_url='/accounts/login/?next=/')
def new_projects(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectUpload(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
            return redirect('home')
    else:
        form = ProjectUpload()
        return render(request,'projects/new_post.html',{"form":form})

def search_project(request):

    if 'search' in request.GET and request.GET["search"]:

        search_term = request.GET.get("search")
        searched_projects = Post.objects.filter(title__icontains=search_term)
        message = f"{search_term}"
        return render(request, 'projects/search.html',{"message":message, "projects":searched_project})

    else:
        message = "You haven't searched for any term "
        return render(request, 'projects/search.html',{"message":message})


def update_profile(request):
     user_profile = Profile.objets.get(user=request.user)

     if request.method =='POST':
         form = UploadProfileForm(request.POST,request.FILES)
         if form.is_valid():
             form.save()
         return redirect('home')
     else:
        form = UpdateProfileForm(instance=request.user.profile)
        return render(request, 'projects/update-prof.html',{'form': form})

def profile_info(request):

    current_user = request_user
    profile_user = Profile.objects.filter(user=current_user).first()
    projects = request.user.post.all()


    return render(request, 'projects/profile.html',{"projects":projects,"profile":profile_info,"current_user":current_user})



class PostViewset(viewsets.ModelViewSet):
    '''
    API endpoint that allowsone to view the detaails of projects posted
    '''

    querryset = Post.objects.all().order_by()



class ProfileViewset(viewsets.ModelViewSet):
    '''
    API endpoint that allows one to view the details of profiles
    '''

    querryset = Profile.objects.all()


def review_rating(request, id):
    current_user = request.user

    current_project = Post.objects.get(id=id)

    if request.method == 'POST':
        form = ProjectRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project = current_project
            rating.user = current_user
            rating.save()
            return redirect('project', id)
    else:
        form = ProjectRatingForm()

    return render(request, 'projects/rating.html', {'form': form, "project": current_project, "user": current_user})


def single_project(request, c_id):
    current_user = request.user
    current_project = Post.objects.get(id=c_id)
    ratings = Rating.objects.filter(post_id=c_id)
    usability = Rating.objects.filter(post_id=c_id).aggregate(Avg('usability_rating'))
    content = Rating.objects.filter(post_id=c_id).aggregate(Avg('content_rating'))
    design = Rating.objects.filter(post_id=c_id).aggregate(Avg('design_rating'))

    return render(request, 'projects/project.html',
                  {"project": current_project, "user": current_user, 'ratings': ratings, "design": design,
                   "content": content, "usability": usability})