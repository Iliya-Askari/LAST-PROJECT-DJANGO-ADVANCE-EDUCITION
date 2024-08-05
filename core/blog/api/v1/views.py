from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter , SearchFilter

from blog.models import *
from .serializer import *
from .pagination import *
from .permissions import *
class PostViewset(viewsets.ModelViewSet):
    """
    This class performs all related operations for posts based on view set model without defining the function
    """

    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {"category": ["exact", "in"], "author": ["exact"]}
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]


class CategoryModelViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CtegorySerializer