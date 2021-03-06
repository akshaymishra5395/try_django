"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include #url

from .views import home_page,about_page,contact_page,courses_page,example_page
from blog.views import blog_post_create_view
from accounts.views import login_view,register_view,logout_view

urlpatterns = [
    path('accounts/register/',register_view),
    path('accounts/login/',login_view),
    path('accounts/logout/',logout_view),
	
    path('', home_page),
	path('home/', home_page),
    
   
    
    path('blog/', include('blog.urls')),
    path('blog-new/', blog_post_create_view),
    #re_path(r'^about/$', about_page),
	re_path(r'^about/$', about_page),
	path('contact/', contact_page),
	path('courses/', courses_page),
    path('example/', example_page),
    path('cfe-admin/', admin.site.urls)
]
