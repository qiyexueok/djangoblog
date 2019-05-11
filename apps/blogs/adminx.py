# -*- coding:utf-8 -*- 
__author__ = 'll'
__date__ = '19-5-8 上午10:27'

import xadmin

from .models import Banner, BlogCategory, Post, Tags, Comment, FriendlyLink


class BannerAdmin(object):
    pass


class BlogCategoryAdmin(object):
    pass


class PostAdmin(object):
    style_fields = {'content': 'ueditor'}


class TagsAdmin(object):
    pass


class CommentAdmin(object):
    pass


class FriendlyLinkAdmin(object):
    pass


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(BlogCategory, BlogCategoryAdmin)
xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Tags, TagsAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(FriendlyLink, FriendlyLinkAdmin)
