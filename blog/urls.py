from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="index"),
    path("posts/", views.AllPostsView.as_view(), name="all_posts"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="single_post"),
    path("read-later", views.ReadLaterView.as_view(), name="read_later")
]