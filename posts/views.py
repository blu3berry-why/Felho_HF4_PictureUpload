from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def posts_lists(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post, 'user': request.user})


def delete_page(request, slug):
    if request.method == 'POST':
        post = Post.objects.get(slug=slug)
        post.delete()
    return redirect('posts:list')


@login_required(login_url='/users/login/')
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', {'form': form})


def posts_sort_name(request):
    posts = Post.objects.all().order_by('-title')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def posts_sort_date(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})