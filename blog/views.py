from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class PostListView(ListView):
    context_object_name = 'all_post'
    model = Post
    template_name = 'blog/home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
