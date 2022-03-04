from ckeditor.fields import RichTextField
from django.db import models


'''
set of custom models to use in apps
'''


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(active=True)


class BaseModel(models.Model):
    """
    a abstract model - it's preferred for all models to inheritance from this model
    """
    description = RichTextField(verbose_name='Description', blank=True)
    active = models.BooleanField(verbose_name='Active Status', default=True)
    updated_time = models.DateTimeField(verbose_name='Modified On', auto_now=True)
    created_time = models.DateTimeField(verbose_name='Creation On', auto_now_add=True, db_index=True)

    objects = models.Manager()
    actives = ActiveManager()

    class Meta:
        abstract = True
