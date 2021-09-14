from django import forms
from user_admin.models import Author , BlogPost, images
from django.utils import timezone

class ImageForm(forms.ModelForm):
    class Meta:
        model = images
        fields = [
            'document'
        ] 

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'author',
            'title',
            'body',
            'links',
            'image'

            ]


    # author = forms.ModelChoiceField(queryset=Author.objects.all())
    # title = forms.CharField( required=True)
    # body = forms.CharField(widget=forms.Textarea, required=True)
    # links = forms.URLField(required=False)
   




class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name',
            'title'
        ]
