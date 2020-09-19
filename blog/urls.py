from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, LoginView, LogoutView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/create-post/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/update-post/', PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete-post/', PostDeleteView.as_view(), name='delete_post'),

    #for Login
    path('login/', LoginView.as_view(), name='login'),
]
