# -*- coding:utf-8 -*- 
__author__ = 'll'
__date__ = '19-5-9 下午3:46'

import string
import random

from django.core.mail import send_mail
from djangoblog.settings import EMAIL_FROM

from users.models import EmailVerifyRecord


def my_send_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == 'update':
        code = make_random_str(4)
    else:
        code = make_random_str()
    email_record.email = email
    email_record.code = code
    email_record.send_type = send_type

    email_record.save()

    if send_type == 'register':
        email_title = "博客注册激活链接"
        email_body = "请点击下列链接激活您的账户http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            print('发送成功')
    elif send_type == 'forget':
        email_title = '博客账户密码重置链接'
        email_body = "请点击下面链接重置密码http://127.0.0.1:8000/forget/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            print('发送成功')
    elif send_type == 'update':
        email_title = "博客账户邮箱更换链接"
        emial_body = "请点击下面链接更换邮箱http://127.0.0.1:8000/update/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [eamil])
        if send_status:
            print('发送成功')




def make_random_str(random_length=16):
    str = ''
    chars = string.ascii_letters + string.digits
    length = len(chars) -1
    for i in range(random_length):
        str += chars[random.randint(0,length)]
    return str

# make_random_str()
# my_send_email('527340771@qq.com')