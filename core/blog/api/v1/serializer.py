from rest_framework import serializers
from ...models import *

class CtegorySerializer(serializers.ModelSerializer):
    """
    this is a class to define category for blog app
    """

    class Meta:
        model = Category
        fields = ["id", "name"]

class PostSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        many=False, slug_field="first_name", read_only=True
    )
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "image",
            "category",
            "status",
            "absolute_url",
            "created_date",
            "published_date",
        ]

    def get_absolute_url(self, obj):
        """
        Get the full address of the posts
        """
        request = self.context.get("request")
        return request.build_absolute_uri(obj.id)