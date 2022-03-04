import random

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from utils.custom_models import BaseModel


class PostTag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField("Slug", max_length=140)

    created = models.DateTimeField("Created", auto_now_add=True)
    modified = models.DateTimeField("Modified", auto_now=True)

    class Meta:
        verbose_name = 'Post Tag'
        verbose_name_plural = 'Posts Tags'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(PostTag, self).save(*args, **kwargs)


def category_image_rename(instance, filename):
    return "%s/%s-%s.%s" % (
        "post/category/banner/", instance.title, random.randint(1, 1000), filename.split('.')[-1])


class PostCategory(BaseModel):
    title = models.CharField(max_length=200,
                             verbose_name='category title')
    category_image = models.ImageField(upload_to=category_image_rename,
                                       blank=True,
                                       null=True,
                                       verbose_name='category_image')
    banner = models.ImageField(upload_to=category_image_rename,
                               verbose_name='category banner',
                               null=True,
                               blank=True)

    sort = models.PositiveIntegerField("sort on list",
                                       default=0)
    short_description = models.CharField('short description', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Post Category"
        verbose_name_plural = "Post Categories"
        ordering = ('sort',)

    def __str__(self):
        return self.title


def post_image_rename(instance, filename):
    return "%s/%s/%s/%s.%s" % (
        "blog/post", instance.title, 'image', random.randint(1, 1000), filename.split('.')[-1])


def post_file_rename(instance, filename):
    return "%s/%s/%s/%s.%s" % ("blog/post", instance.title, 'file', random.randint(1, 1000), filename.split('.')[-1])


class Post(BaseModel):
    STATUS_IS_DELETE = -3
    STATUS_WAIT_FOR_APPROVE = -2
    STATUS_NEED_TO_EDIT = -1
    STATUS_DRAFT = 0
    STATUS_IS_PUBLISHED = 1
    STATUS = (
        (STATUS_IS_DELETE, "delete"),
        (STATUS_WAIT_FOR_APPROVE, "wait for approve"),
        (STATUS_NEED_TO_EDIT, "need to edit"),
        (STATUS_DRAFT, "draft"),
        (STATUS_IS_PUBLISHED, "published"),
    )

    status = models.SmallIntegerField(choices=STATUS,
                                      default=STATUS_DRAFT,
                                      verbose_name='status')
    title = models.CharField(max_length=200,
                             verbose_name='post title')
    short_content = RichTextField(verbose_name="short content",
                                  blank=True,
                                  null=True)
    button_text = models.CharField('button text', max_length=150, default='READ MORE!')
    is_selected = models.BooleanField('selected', default=False)
    post_image = models.ImageField(upload_to=post_image_rename,
                                   verbose_name='post image',
                                   null=True,
                                   blank=True)
    post_icon = models.FileField(upload_to=post_image_rename,
                                 verbose_name='post icon',
                                 null=True,
                                 blank=True)
    user = models.ForeignKey(User, verbose_name="author",
                             related_name="posts",
                             on_delete=models.CASCADE,
                             editable=False)
    category = models.ForeignKey(PostCategory,
                                 verbose_name="post category",
                                 related_name="posts",
                                 on_delete=models.CASCADE)
    related_posts = models.ManyToManyField('self',
                                           verbose_name="related posts",
                                           blank=True)

    extra_file = models.FileField('extra file', upload_to=post_file_rename, null=True, blank=True)
    slug = models.SlugField("Slug", max_length=140, allow_unicode=True, editable=False, blank=True)
    tags = models.ManyToManyField(PostTag, verbose_name="Post Tags")

    def __str_(self):
        return self.title

    @property
    def get_upload_url(self):
        if self.extra_file:
            return self.extra_file.url
        return '#'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        # ordering = ['-created_time']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)
