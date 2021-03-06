#coding:utf-8
"""
    博客的评论功能?
"""
from django import forms
#  借此加入博客的评论功能


class CommentForm(forms.Form):
    name = forms.CharField(label='称呼',max_length=50,error_messages={
        'required':'请填写您的称呼',
        'max_length':'称呼太长啊'
    })
    email = forms.EmailField(label='邮箱', error_messages={
        'required': '请填写您的邮箱',
        'invalid': '邮箱格式不正确'
    })
    content = forms.CharField(label='评论内容', max_length=5000, error_messages={
        'required': '请填写您的评论内容',
        'max_length': '评论内容超长了'
    })