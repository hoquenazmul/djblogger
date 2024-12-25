from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
]
