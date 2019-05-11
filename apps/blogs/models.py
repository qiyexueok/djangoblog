from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField

from users.models import BlogUser


#轮播图
class Banner(models.Model):
    title = models.CharField(default='', max_length=50, verbose_name='标题')
    image = models.ImageField(upload_to='banner', verbose_name='轮播图')
    link_url = models.URLField(max_length=100, verbose_name='图片链接')
    index = models.IntegerField(verbose_name='索引')
    is_active = models.BooleanField(default=False, verbose_name='是否激活')

    class Meta():
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


#博客分类
class BlogCategory(models.Model):
    category = models.CharField(default='', max_length=50, verbose_name='类别')

    class Meta():
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category


#标签
class Tags(models.Model):
    name = models.CharField(default='', max_length=30, verbose_name='标签')

    class Meta():
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#博客
class Post(models.Model):
    user = models.ForeignKey(BlogUser, verbose_name='用户')
    category = models.ForeignKey(BlogCategory, verbose_name='博客类型')
    tags = models.ManyToManyField(Tags, verbose_name='标签')
    title = models.CharField(default='', max_length=50, verbose_name='标题')
    content = UEditorField(width=800, height=600, imagePath='post/images/', filePath='post/files/',verbose_name='内容')
    pub_date = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    cover = models.ImageField(upload_to='post/covers', verbose_name='博客封面')
    visits = models.IntegerField(default=0, verbose_name='访问人数')
    recommend = models.BooleanField(default=False, verbose_name='是否推荐')

    class Meta():
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


#评论
class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name='博客')
    user = models.ForeignKey(BlogUser, verbose_name ='用户')
    pub_date = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    content = models.TextField(verbose_name='内容')

    class Meta():
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


#友情链接
class FriendlyLink(models.Model):
    title = models.CharField(default='', max_length=50, verbose_name='标题')
    url = models.URLField(default='', max_length=50, verbose_name='链接')

    class Meta():
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title







