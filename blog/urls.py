from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.posts, name="all_posts"),
    path("posts/<str:post>", views.post, name="single_post")
]