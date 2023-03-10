from django.urls import path
from feed import views
from feed.views import PostUpdateView, PostListView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='feed-home'),
    path('post/new', views.create_post, name='post-create'),
    path('post/<int:pk>', views.post_detail, name='post-detail'),
    path('like', views.like, name='post-like'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.post_delete, name='post-delete'),
    path('search/', views.search_posts, name='search_posts'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
]