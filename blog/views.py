from django.views.generic import ListView

from .models import Post, PostCategory


class PostsListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'pages/our-story.html'
    page_name = 'posts'

    def get_context_data(self, **kwargs):
        posts = Post.objects.filter(status=Post.STATUS_IS_PUBLISHED).all()

        context = super(PostsListView, self).get_context_data(**kwargs)

        context['posts'] = posts
        print(posts)
        context['category'] = PostCategory.objects.filter().first()

        return context
