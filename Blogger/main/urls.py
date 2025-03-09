from django.urls import path
from . import views

app_name='main'

urlpatterns=[
    path("home/",views.home, name='main'),
    path("new_post/",views.new_post, name='new_post'),
    path("details/<post_id>/", views.details, name="details"),
    path("update/<post_id>/", views.posts_update , name="posts_update"),
    path("delete /<post_id>/", views.posts_delete,name="posts_delete"),

]