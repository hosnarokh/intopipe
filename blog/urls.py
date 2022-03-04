from django.urls import re_path

from .views import PostsListView

app_name = 'posts'
urlpatterns = [
    re_path(r'^$', PostsListView.as_view(), name='post_list')
]
