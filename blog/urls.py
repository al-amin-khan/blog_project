from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, LoginView, LogoutView

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='detail'),
    path('post/post/create-post/', PostCreateView.as_view(), name='create_post'),
    path('post/<str:slug>/update-post/', PostUpdateView.as_view(), name='update_post'),
    path('post/<str:slug>/delete-post/', PostDeleteView.as_view(), name='delete_post'),

    #for Login
    path('login/', LoginView.as_view(), name='login'),
]
