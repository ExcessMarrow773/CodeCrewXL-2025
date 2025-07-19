from django.shortcuts import render, redirect, get_object_or_404
from app.models import Post, Comment
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from app.forms import CommentForm, CreatePost
from app.AI import AI

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "app/index.html", context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {
        'user': request.user,
        'posts': Post.objects.filter(author=request.user.username).order_by('-created_on')
    }
    return render(request, 'profile.html', context)

# Post things

def category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "app/category.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=request.user.username,
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "app/detail.html", context)

def makepost(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = Post(
                author=request.user.username,
                title=form.cleaned_data["title"],
                body=form.cleaned_data["body"],
                image=form.cleaned_data["image"]
            )
            post.save()
            post.categories.set(form.cleaned_data["categories"])
            post.save()
            return redirect('index')
    else:
        form = CreatePost()
    
    return render(request, 'app/makepost.html', {'form': form})

def journal(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {
        'user': request.user,
        'posts': Post.objects.filter(author=request.user.username).order_by('-created_on'),
        'comments': Comment.objects.filter(post__author=request.user.username).order_by('-created_on'),
        'ai': AI()  # Assuming AI is a class that handles AI-related tasks
    }
    return render(request, 'journal.html', context)




class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    template_name = 'index.html'
