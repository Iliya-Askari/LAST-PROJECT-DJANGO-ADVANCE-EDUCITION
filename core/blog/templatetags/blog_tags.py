from django import template
from blog.models import Category
from django.utils import timezone
from blog.models import  Post
register=template.Library()


@register.inclusion_tag('blog/blog-category.html')
def postcategotys():
   currnt_time=timezone.now()
   posts = Post.objects.filter(status=1)
   categories = Category.objects.all()
   cat_dict = {}
   for category in categories:
      if posts.filter(category=category).exists():  
         cat_dict[category.name] = posts.filter(category=category).count()
   return {'categories': cat_dict}


@register.inclusion_tag('blog/latest_posts.html')
def lastposts(arg=5):
    currnt_time=timezone.now()
    posts=Post.objects.filter(status=1 , published_date__lte=currnt_time).order_by('-published_date')[:arg]
    return {'posts':posts}


@register.inclusion_tag('home/recent-blog.html')
def recent (arg=3):
   currnt_time=timezone.now()
   posts = Post.objects.filter(status=1 , published_date__lte=currnt_time).order_by('-published_date')[:arg]
   context = {'posts' : posts}
   return context