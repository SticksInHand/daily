# -*- coding:utf-8 -*-
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)   # 文章题目
    category = models.CharField(max_length=50, blank=True)   # 文章标签
    date_time = models.CharField(max_length=8)  # 文章日期
    images = models.CharField(max_length=255)  # 文章配图
    content = models.TextField(blank=True, null=True)  # 文章正文

    def __str__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-date_time']
