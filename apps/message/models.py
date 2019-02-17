#coding: utf-8
from django.db import models

class UserMessage(models.Model):
    object_id = models.CharField(max_length=50, primary_key=True, verbose_name='主键', default='')
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'用户名')
    email = models.EmailField(verbose_name=u'邮箱')
    address = models.CharField(max_length=50, verbose_name=u'联系地址')
    message = models.CharField(max_length=100, verbose_name=u'留言信息')

    class Meta:
        db_table = 'user_message'
        ordering = ('-object_id',)
        verbose_name_plural = u'用户留言信息'
