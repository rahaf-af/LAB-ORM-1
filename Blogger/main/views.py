from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import post

# Create your views here.

def home(request:HttpRequest):

    return render(request, 'main/home.html/')


def new_post(request:HttpRequest):

    create_post=post(title='my first sql project !!',content='I am very happy to share with you that I have finally started my first project using the database and I am confident that this project is the beginning and that I have a bright future full of achievements',is_published=True,published_at='2025-03-06')
    create_post.save()

    return render(request, 'main/new_posts.html/')
