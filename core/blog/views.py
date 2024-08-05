from django.shortcuts import render
from django.views.generic import ListView , TemplateView , DetailView , DeleteView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from .models import *
from django.contrib import messages

class BlogHome(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        currnt_time = timezone.now()
        posts = Post.objects.filter(published_date__lte=currnt_time, status=1)
        
        cat_name = self.kwargs.get('cat_name')
        tag_name = self.kwargs.get('tag_name')
        author_username = self.kwargs.get('author_username')
        
        if cat_name:
            posts = posts.filter(category__name=cat_name)
        if tag_name:
            posts = posts.filter(tag__name__in=[tag_name])
        
        return posts

class PostSearchView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        current_time = timezone.now()
        posts = Post.objects.filter(status=1, published_date__lte=current_time)

        query = self.request.GET.get('s', '')
        if query:
            posts = posts.filter(content__icontains=query)

        if not posts.exists() and query:
            messages.add_message(self.request, messages.ERROR, 'The desired phrase was not found. Please try again')
            return Post.objects.none()

        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('s', '')
        return context

class BlogSingleView(DetailView):
    model = Post
    template_name = 'blog/blog-details.html'
    context_object_name = 'post'

    def get_queryset(self):
        current_time = timezone.now()
        return Post.objects.filter(status=1, published_date__lte=current_time)

    def get_object(self):
        pid = self.kwargs.get('pid')
        post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=timezone.now())
        post.counted_views += 1
        post.save()
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class DeleteBlogView(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = "delete"
    success_url = reverse_lazy("blog:blog")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        profile = Profile.objects.filter(user=self.request.user).first()
        if not profile:
            raise Http404("Profile does not exist")
        return self.model.objects.filter(author=profile)
