from django.shortcuts import render
from user_admin.models import Author, BlogPost
from user_admin.forms import AuthorForm, BlogPostForm, ImageForm


from django.shortcuts import render, HttpResponseRedirect, Http404, reverse

# view for creating a blog post
def add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
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


def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('landing'))
    else:
        form = ImageForm()
    return render(request, 'generic_form.html', {'form': form})