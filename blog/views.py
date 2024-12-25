from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def home(request):
    context = {
        'object_list': Post.objects.all()
    }
    return render(request, 'blog/post_list.html', context)


class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']
    # template_name = 'blog/home.html' # if not <app>/<model>_<viewtype>.html
    # context_object_name = 'posts' # if it's not `object_list`
