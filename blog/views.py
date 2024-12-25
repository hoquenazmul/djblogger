from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post


class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']
    # template_name = 'blog/home.html' # if not <app>/<model>_<viewtype>.html
    # context_object_name = 'posts' # if it's not `object_list`


class PostDetailView(DetailView):
    model = Post
    

def about(request):
    context = {
        'page': 'About'
    }
    
    return render(request, 'blog/coming_soon.html', context)

def contact(request):
    context = {
        'page': 'Contact'
    }
    
    return render(request, 'blog/coming_soon.html', context)
