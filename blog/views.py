from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
class PostListView(ListView):
    context_object_name = 'all_post'
    model = Post
    template_name = 'blog/home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    fields = ['title', 'body']
