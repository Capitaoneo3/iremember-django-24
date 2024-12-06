"""
URL configuration for iremember project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from myapp.views.home_view import index, info_page
from myapp.views.auth_view import login_view, register_view
from myapp.views.user_view import user_details
from myapp.views.create_post_view import create_post

urlpatterns = [
    path('', create_post, name='create_post'),
    path('info/', info_page, name='info'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('user-details/', user_details, name='user_details'),

]
