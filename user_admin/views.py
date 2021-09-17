from django.shortcuts import render
from user_admin.models import Author, BlogPost
from user_admin.forms import AuthorForm, BlogPostForm, ImageForm,LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User


from django.shortcuts import render, HttpResponseRedirect, Http404, reverse

# view for creating a blog post
@login_required()
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
@staff_member_required
def add_author(request):
    staff = User.objects.filter(is_staff=True)
    if not staff:
        return HttpResponseRedirect(reverse("homepage"))
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
        
        newuser = User.objects.create_user(
                username=data["name"], password=data['password'])  # noqa
        Author.objects.create(name=data["name"], title=data["title"])
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

def login_view(request):
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(
                request, username=data["username"], password=data["password"])
            if user:

                login(request, user)

                return HttpResponseRedirect(request.GET.get("next", reverse("createpost")))  # noqa

        form = LoginForm()

        return render(request, "generic_form.html", {"form": form})

def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse("landing"))