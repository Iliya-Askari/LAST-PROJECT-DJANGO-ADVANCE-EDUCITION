from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('', BlogHome.as_view(), name='blog'),
    path('category/<str:cat_name>/', BlogHome.as_view(), name='category'),
    path('tag/<str:tag_name>/', BlogHome.as_view(), name='blog_tag'),
    path('author/', BlogHome.as_view(), name='author'),
    path('details/<int:pid>/', BlogSingleView.as_view(), name='details'),
    path('search/', PostSearchView.as_view(), name='search'),
    path('details/<int:pk>/delete/', DeleteBlogView.as_view(), name='delete'),
]
