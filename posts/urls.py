from django.urls import path
from . import views


app_name = 'posts'


urlpatterns = [
    path('', views.posts_lists, name='list'),
    path('new-post/', views.post_new, name='new-post'),
    path('sort/name', views.posts_sort_name, name='sort_name'),
    path('sort/date', views.posts_sort_date, name='sort_date'),
    path('delete/<slug:slug>', views.delete_page, name='delete'),

    # Need to put everything before the slug! Because if you put it after the slug will catch everything
    # slug is an individual name for a post after the '/' like posts/my-first-post
    path('<slug:slug>', views.post_page, name='page'),


]

