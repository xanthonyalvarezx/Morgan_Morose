from django.db import models
from django.utils import timezone

# model to create an autor object
class Author(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=10, blank=True)


    def __str__(self):
        return self.name

# model to create a blog post
class BlogPost(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField( max_length=100)
    body = models.TextField()
    links = models.URLField()
    created = models.DateTimeField(default=timezone.now)
    image = models.FileField(upload_to='images/')

class images(models.Model):
    document = models.FileField(upload_to='images/')