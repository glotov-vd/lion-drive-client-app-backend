from django.urls import re_path, path

from comments import views

urlpatterns = [
    re_path(r'^+/comments', views.get_post_comments, name='comments_list'),
]