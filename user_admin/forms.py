from django import forms
from user_admin.models import Author
from django.utils import timezone

class BlogPostForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    title = forms.CharField( required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)
    links = forms.URLField(required=False)



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name',
            'title'
        ]
