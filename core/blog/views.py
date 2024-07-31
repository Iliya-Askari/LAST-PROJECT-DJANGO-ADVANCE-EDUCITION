from django.shortcuts import render
from django.views.generic import ListView , TemplateView , DetailView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post

class BlogHome(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 3

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
        if author_username:
            posts = posts.filter(author__username=author_username)
        
        return posts


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
        pid = self.object.pk
        current_time = timezone.now()
        context['next_post'] = Post.objects.filter(id__gt=pid, status=1, published_date__lte=current_time).order_by('id').first()
        context['prev_post'] = Post.objects.filter(id__lt=pid, status=1, published_date__lte=current_time).order_by('-id').first()
        return context
    

