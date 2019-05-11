# -*- coding:utf-8 -*- 
__author__ = 'll'
__date__ = '19-5-8 上午10:27'

import xadmin
from .models import BlogUser, EmailVerifyRecord


class BlogUserAdmin(object):
    pass


class EmailVerifyRecordAdmin(object):
    pass

xadmin.site.unregister(BlogUser)
xadmin.site.register(BlogUser, BlogUserAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)