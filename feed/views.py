from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import json

from feed.forms import NewPostForm, NewCommentForm
from feed.models import Post, Comment, Like


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'feed/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            liked = [i for i in Post.objects.all() if Like.objects.filter(user=self.request.user, post=i)]
            context['liked_post'] = liked
        return context


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    templates_name = 'feed/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        liked = [i for i in Post.objects.filter(user=user) if Like.objects.filter(user=self.request.user, post=i)]
        context['liked_post'] = liked
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(user=user).order_by('-date_posted')


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    comments = Comment.objects.filter(post=post)
    is_liked = Like.objects.filter(user=user, post=post)
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.post = post
            data.user = user
            data.save()
            return redirect('post-detail', pk=pk)
    else:
        form = NewCommentForm()
    args = {
        'post': post,
        'form': form,
        'is_liked': is_liked,
        'comments': comments,
    }
    return render(request, 'feed/post_detail.html', args)


@login_required
def create_post(request):
    user = request.user
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = user
            data.save()
            messages.success(request, f'Posted Successfully')
            return redirect('feed-home')
    else:
        form = NewPostForm()
    args = {
        'form': form,
    }
    return render(request, 'feed/create_post.html', args)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'feed/create_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user == post.user:
        Post.objects.get(pk=pk).delete()
    return redirect('feed_home')


@login_required
def search_posts(request):
    posts = Post.objects.all().order_by('-date_posted')
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__icontains=query) |
            Q(user__username__icontains=query)
        ).distinct()
    args = {
        'posts': posts
    }

    return render(request, 'feed/search_posts.html', args)


@login_required
def like(request):
    post_id = request.GET.get("likeId", "")
    user = request.user
    print(user)
    post = Post.objects.get(pk=post_id)
    liked = False
    internal_like = Like.objects.filter(user=user, post=post)
    if internal_like:
        internal_like.delete()
    else:
        liked = True
        Like.objects.create(user=user, post=post)
    args = {
        'liked': liked,
        'count': post.likes.count(),
    }

    response = json.dumps(args)
    return HttpResponse(response, content_type="application/json")
