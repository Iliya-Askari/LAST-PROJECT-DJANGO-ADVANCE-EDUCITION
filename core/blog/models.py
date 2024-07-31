from django.contrib.auth import get_user_model
from django.db import models

from django.urls import reverse
from taggit.managers import TaggableManager

from accounts.models import Profile
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(upload_to='blog/' , default='blog-1.jpg')
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL , null=True)
    content = models.TextField()
    tag = TaggableManager()
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_required = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    uptodate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.title,self.id)
    
    class Meta:
        ordering=['-created_date']
    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})