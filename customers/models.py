import random

from django.contrib.auth.models import User
from django.db import models

from utils.custom_models import BaseModel


def order_file_rename(instance, filename):
    return "%s/%s/%s/%s.%s" % (
        "customer/order", 'file', instance.name, random.randint(1, 1000000), filename.split('.')[-1])


class Customer(BaseModel):
    STATUS_IS_PENDING = 0
    STATUS_IS_VERIFIED = 1
    STATUS = (
        (STATUS_IS_PENDING, "pending"),
        (STATUS_IS_VERIFIED, "verify"),
    )

    status = models.SmallIntegerField(choices=STATUS,
                                      default=STATUS_IS_PENDING,
                                      verbose_name='status')
    name = models.CharField(max_length=200,
                            verbose_name='name')
    email = models.EmailField('email')

    website = models.URLField('website', max_length=200, null=True, blank=True)
    logo = models.FileField('logo', upload_to=order_file_rename, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True,
                            verbose_name='phone')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Material(BaseModel):
    title = models.CharField(max_length=200,
                             verbose_name='title')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"


class Order(BaseModel):
    STATUS_IS_PENDING = 0
    STATUS_IS_VERIFIED = 1
    STATUS = (
        (STATUS_IS_PENDING, "pending"),
        (STATUS_IS_VERIFIED, "verify"),
    )

    status = models.SmallIntegerField(choices=STATUS,
                                      default=STATUS_IS_PENDING,
                                      verbose_name='status')
    customer = models.ForeignKey('Customer', verbose_name='customer', related_name='orders', on_delete=models.CASCADE)
    material = models.ForeignKey('Material', verbose_name='material', related_name='orders', on_delete=models.CASCADE)
    inner_diameter = models.FloatField('inner diameter')
    thickness = models.FloatField('thickness')
    length = models.FloatField('length')
    quantity = models.PositiveIntegerField('quantity', default=1)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"
