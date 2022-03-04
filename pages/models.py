import random

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

from utils.custom_models import BaseModel


class Contact(BaseModel):
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    company = models.CharField('Company', max_length=100)
    email = models.EmailField('Email')
    phone_number = models.CharField('Phone Number', max_length=20)
    message = RichTextField(verbose_name='Message')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


def feature_file_rename(instance, filename):
    return "%s/%s/%s.%s" % ("home/feature", 'file', random.randint(1, 1000), filename.split('.')[-1])


class HomeFeature(BaseModel):
    button_text = models.CharField('button text', max_length=150, default=' TOUCH HERE!')
    extra_file = models.FileField('extra file', upload_to=feature_file_rename, null=True, blank=True)

    class Meta:
        verbose_name = 'Home Feature'
        verbose_name_plural = 'Home Features'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        HomeFeature.objects.all().update(active=False)
        super(HomeFeature, self).save(force_insert, force_update, using, update_fields)

    @property
    def get_upload_url(self):
        if self.extra_file:
            return self.extra_file.url
        return '#'

