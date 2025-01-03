from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Post


class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']
    paginate_by = 4
    # template_name = 'blog/home.html' # if not <app>/<model>_<viewtype>.html
    # context_object_name = 'posts' # if it's not `object_list`


class UserPostListView(ListView):
    model = Post
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


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

     
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

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
