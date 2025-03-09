from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import post

# Create your views here.

def home(request:HttpRequest):
    #get all post
    posts=post.objects.all()[0:3]
    return render(request, 'main/home.html/',{"posts":posts})


def new_post(request:HttpRequest):

    if request.method=="post":
        create_post=post(title=request.post["title"],content=request.post["content"],is_published=request.post["is_published"],published_at=request.post["published_at"] , poster=request.FILES["poster"])
        create_post.save()
        return redirect('main:home')

    return render(request, 'main/new_posts.html/')

def details(request:HttpRequest , post_id:int):
    post_info= post.objects.get(pk=post_id)
    

    return render(request ,'main/details.html/',{"post_info":post} )

def posts_update(request:HttpRequest , post_id:int):
     update_info= post.objects.get(pk=post_id)

     if request.method=="POST":
         update_info.title=request.POST["title"]
         update_info.content=request.POST["content"]
         update_info.is_published=request.POST["is_publishe"]
         update_info.published_at=request.POST["published_at"]
         if "poster" in request.FILES:post.poster= request.FILES["poster"]
       # update_info.poster=request.POST["poster"]
        update_info.save()
     

     return redirect("main:update", post_id=post.id)
         

     return render(request ,'main/update.html/',{"update_info":post} )

def posts_delete(request:HttpRequest , post_id:int):
     delete_post= post.objects.get(pk=post_id)
     delete_post.delete()
     
     return redirect("main:home")

def all_posts(request:HttpRequest):
    #get all post
    posts=post.objects.all()
    return render(request, 'main/all_post.html/',{"posts":posts})
