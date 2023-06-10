"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views

app_name = "portfolio"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_page_view, name='home'),
    path('aboutme/', views.about_me_view, name='aboutme'),
    path('projects/', views.projects_view, name='projects'),
    path('wp/', views.wp_view, name='wp'),
    path('blog/', views.blog_view, name='blog'),
    path('atw/', views.atw_view, name='atw'),
    path('more/', views.more_view, name='more'),
    path('contact/', views.contact_view, name='contact'),
]
