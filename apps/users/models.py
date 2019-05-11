from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


#用户
class BlogUser(AbstractUser):
    nickname = models.CharField(default='', max_length=20, verbose_name='昵称')


#邮箱验证
class EmailVerifyRecord(models.Model):
    code = models.CharField(default='', max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(default='register', max_length=20, choices=(('register','注册'), ('forget', '找回密码'), ('update', '修改邮箱')), verbose_name='验证类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta():
        verbose_name = '邮箱验证'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0} {1}'.format(self.email, self.code)


#
