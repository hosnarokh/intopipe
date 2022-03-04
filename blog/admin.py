from django.contrib import admin

from .models import Post, PostCategory


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_content', 'user', 'slug', 'status', 'active']
    search_fields = ('title',)
    list_filter = ['status', 'user']
    readonly_fields = ['updated_time', 'created_time', 'slug', ]
    fields = ['title',
              'slug',
              ('status', 'is_selected', 'active',),
              'extra_file',
              'post_image',
              'post_icon',
              'category',
              'related_posts',
              ('updated_time', 'created_time'),
              'button_text',
              'short_content',
              'description']
    exclude = ['user', ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
        super(PostAdmin, self).save_model(request, obj, form, change)


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    search_fields = ('title',)
    readonly_fields = ['updated_time', 'created_time', ]
    fields = ['title',
              'category_image',
              'banner',
              'sort',
              'active',
              'created_time',
              'updated_time',
              'description']
