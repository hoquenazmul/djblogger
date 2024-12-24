from django.shortcuts import render


def hello(request):
    return render(request, 'blog/post_list.html')
