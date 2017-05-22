# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode


class Teachers(models.Model):
    class Meta:
        verbose_name = 'Teachers'
        verbose_name_plural = 'Teachers'

    name = models.CharField(max_length=255, verbose_name='FIO')
    image = models.ImageField(upload_to='images/teachers', verbose_name='upload image')
    email = models.EmailField(verbose_name='Email')
    number = models.CharField(max_length=255, verbose_name='Cell Phone Number')

    def __unicode__(self):
        return smart_unicode(self.name)


class Publication(models.Model):
    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    title = models.CharField(max_length=255, verbose_name='title')
    text = models.TextField(verbose_name='text')
    image = models.ImageField(upload_to='public/images', verbose_name='Image')

    def __unicode__(self):
        return smart_unicode(self.title)
