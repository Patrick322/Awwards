from django.shortcuts import render

# Create your views here.
from .models import *
from .forms import ProjectUpload,ProfileForm
from django.contrib.auth.decorators import login _required
from rest_framework import viewsets
from .serializers import PostSerializer,ProfileSerializer

def home(request):
    projects = Post.objects.all()
    return render(request, 'myprojects/index.html',{"projects":projects})

@login_required (login_url='/accounts/login/?next=/')
    