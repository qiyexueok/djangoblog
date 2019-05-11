# -*- coding:utf-8 -*- 
__author__ = 'll'
__date__ = '19-5-8 下午11:53'

from django import forms
from DjangoUeditor.forms import UEditorField

from .models import Post


class TestUEditorForm(forms.Form):
    content = UEditorField('内容', width=900, height=600, toolbars="full", imagePath="post/images/", filePath="post/files/",upload_settings={"imageMaxSize":1204000}, settings={})


class BlogForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = [ 'category','tags','title','content', 'cover']



