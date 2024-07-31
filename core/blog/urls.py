from django.urls import path
from .views import *
app_name = "blog"
urlpatterns = [
    path('', BlogHome.as_view(), name='blog'),
    path('category/<str:cat_name>/', BlogHome.as_view(), name='category'),
    path('tag/<str:tag_name>/', BlogHome.as_view(), name='blog_tag'),
    path('author/<str:author_username>/', BlogHome.as_view(), name='author'),
    path('details/<int:pid>/', BlogSingleView.as_view(), name='details'),

]
