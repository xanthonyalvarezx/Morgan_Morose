from django.contrib import admin
from user_admin.models import Author, BlogPost, images
# Register your models here.
admin.site.register(Author)
admin.site.register(BlogPost)
admin.site.register(images)