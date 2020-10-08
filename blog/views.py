from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class PostListView(ListView):
    context_object_name = 'all_post'
    model = Post
    # success_url = 'blog:home'
    template_name = 'blog/home.html'

class PostDetailView(DetailView):
    model = Post
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = 'blog:detail'
    template_name = 'blog/detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    login_required = True
    template_name = 'blog/create_post.html'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    fields = ['title', 'body']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = '/'

class LoginView(LoginView):
    template_name = 'registration/login.html'
