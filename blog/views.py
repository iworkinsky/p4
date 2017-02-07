#codiing:utf-8
from django.shortcuts import render
from blog.models import *
from blog.forms import CommentForm
from django.http import Http404

# Create your views here.
def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created')
    return render(request,'blog_list.html',{'blogs':blogs})
def get_details(request,blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    #return render(request,'mydebug.html',{'mydc':request.method})
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
            'blog':blog,
            'comments':blog.comment_set.all().order_by('-created'),
            'form':form
    }
    return render(request,'blog_details.html',ctx)
