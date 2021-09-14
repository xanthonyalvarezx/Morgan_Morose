from django.shortcuts import render
from user_admin.models import Author, BlogPost
# Create your views here.
def landing(request):
    posts = BlogPost.objects.all()
    return render(request, 'landing.html', {'posts':posts}  )