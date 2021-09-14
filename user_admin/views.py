from django.shortcuts import render
from user_admin.models import Author, BlogPost
from user_admin.forms import AuthorForm, BlogPostForm


from django.shortcuts import render, HttpResponseRedirect, Http404, reverse

# view for creating a blog post
def add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_post = BlogPost.objects.create(
                author=data['author'],
                title=data['title'],
                body=data['body'],
                links=data['links']
            
            )
        return HttpResponseRedirect(reverse('landing'))
    form = BlogPostForm()
    return render(request, 'generic_form.html', {'form':form})


# view for creating a admin user 
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('landing'))
    form = AuthorForm()
    return render(request, 'generic_form.html', {'form':form})