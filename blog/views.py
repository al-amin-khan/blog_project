from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')

class LoginView(LoginView):
    template_name = 'registration/login.html'
