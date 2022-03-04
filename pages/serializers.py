from rest_framework import serializers

from .models import Contact
# from .models import Post


# class PostListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'short_content', 'post_image', 'user',)
#         read_only_field = ('id',)
#
#
# class CategoryListSerializer(serializers.ModelSerializer):
#     posts = PostListSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = Category
#         fields = ('id', 'title', 'category_image', 'main_category', 'posts')
#         read_only_field = ('id',)
#
#
# class CategoryDetailSerializer(serializers.ModelSerializer):
#     categories = CategoryListSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = Category
#         fields = (
#             'id', 'title', 'description', 'category_image', 'main_category',
#             'categories',)
#         read_only_field = ('id',)
#
#
# class PostDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'short_content', 'post_image', 'user',
#                   'category', 'key_words', 'views', 'related_posts')
#         read_only_field = ('id',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'company', 'email', 'phone_number', 'message')
