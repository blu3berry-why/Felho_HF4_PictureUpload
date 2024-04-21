from django.urls import path
from . import views


app_name = 'posts'


urlpatterns = [
    path('', views.posts_lists, name='list'),
    path('new-post/', views.post_new, name='new-post'),


    # Need to put everything before the slug! Because if you put it after the slug will catch everything
    # slug is an individual name for a post after the '/' like posts/my-first-post
    path('<slug:slug>', views.post_page, name='page'),

]

