from django.shortcuts import render
from .models import Post


def hello(request):
    object_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {'object_list': object_list})
