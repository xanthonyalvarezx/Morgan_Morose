from django.shortcuts import render
from user_admin.models import Author, BlogPost
import re
# Create your views here.

# display posts to the landing page


def landing(request):
    posts = BlogPost.objects.all().order_by("-created")
# only show the latest 10 posts
    return render(request, 'landing.html', {'posts': posts[0:10]})


def music(request):
    posts = BlogPost.objects.filter(catagory="Music").order_by("-created")
    return render(request, 'landing.html', {'posts': posts})


def fashion(request):
    posts = BlogPost.objects.filter(catagory="Fashion").order_by("-created")
    return render(request, 'landing.html', {'posts': posts})


def travel(request):
    posts = BlogPost.objects.filter(catagory="Travel").order_by("-created")
    return render(request, 'landing.html', {'posts': posts})


def food(request):
    posts = BlogPost.objects.filter(catagory="Food").order_by("-created")
    return render(request, 'landing.html', {'posts': posts})


# show post detail / body text on detail page


def post_detail(request, post_id: int):
    posts = BlogPost.objects.get(id=post_id)
    searchImage = re.search("(images\/(\S+))", str(posts.image))

    return render(request, "post_detail.html", {"posts": posts, "searchImage": searchImage[2]})
