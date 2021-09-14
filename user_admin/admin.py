from django.contrib import admin
from user_admin.models import Author, BlogPost
# Register your models here.
admin.site.register(Author)
admin.site.register(BlogPost)