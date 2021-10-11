from django.shortcuts import render
from user_admin.models import Author, BlogPost
import re
# Create your views here.
def landing(request):
    posts = BlogPost.objects.all()
    return render(request, 'landing.html', {'posts':posts}  )

def post_detail(request, post_id: int):
    posts = BlogPost.objects.get(id=post_id)
    searchImage = re.search("(images\/(\S+))",str(posts.image))
    print(searchImage[2])

    return render(request, "post_detail.html", {"posts": posts, "searchImage": searchImage[2]})