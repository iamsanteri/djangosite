from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Post

# Temporary utility function
def get_date(post):
    return post['date']

# Create your views here.
def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
       "all_posts": all_posts
    })

def post(request, slug):
    try:
        identified_post = get_object_or_404(Post, slug=slug)
        return render(request, "blog/single-post.html", {
            "post": identified_post,
            "post_tags": identified_post.tags.all()
        })
    except:
        raise Http404()