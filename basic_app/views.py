from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    return render(request, 'basic_app/home.html', context= {'posts':Post.objects.all()})

def about(request):
    return render(request, 'basic_app/about.html', {'title':'About'})
