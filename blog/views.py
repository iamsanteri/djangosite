from django.shortcuts import render
from django.http import Http404

blog_posts = {
    "My first post": "Welcome dear readers!",
    "My second post": "This is getting very tedious.",
    "My third post": "I'm not sure I want to blog anymore.",
    "My fourth post": "Ok I'm about to quit, it ain't that fun."
}

# Create your views here.
def index(request): 
    posts_snapshot = list(blog_posts.keys())
    return render(request, "blog/index.html", {
        "posts_snapshot": posts_snapshot
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
       "blog_posts": blog_posts
    })

def post (request, post):
    try:
        current_post = blog_posts[post]
        return render(request, "blog/single-post.html", {
            "post_title": post,
            "current_post": current_post
        })
    except:
        raise Http404()