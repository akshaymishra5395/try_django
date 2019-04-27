from django.urls import path,re_path #url

from .views import (blog_post_list_view,blog_post_detail_view,blog_post_delete_view,
blog_post_retreive_view,
blog_post_update_view)

urlpatterns = [
    	path('', blog_post_list_view),
        path('<str:slug>', blog_post_detail_view),
        path('<str:slug>/retreive', blog_post_retreive_view),
        path('<str:slug>/delete', blog_post_delete_view),
        path('<str:slug>/edit', blog_post_update_view),
    ]
