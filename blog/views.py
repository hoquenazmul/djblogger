from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from .models import Post


class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']
    # template_name = 'blog/home.html' # if not <app>/<model>_<viewtype>.html
    # context_object_name = 'posts' # if it's not `object_list`


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

     
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

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
