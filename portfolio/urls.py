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
    path('', views.home_page_view, name='home'),
    path('aboutme/', views.about_me_view, name='aboutme'),
    path('projects/', views.projects_view, name='projects'),
    path('wp/', views.wp_view, name='wp'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/delete/<int:id_post>', views.delete_blog_post, name='delete'),
    path('blog/like/<int:id_post>', views.like_post, name="like"),
    path('blog/deslike/<int:idP>', views.deslike_post, name="deslike"),
    path('atw/', views.atw_view, name='atw'),
    path('more/', views.more_view, name='more'),
    path('contact/', views.contact_view, name='contact'),
    path('login/', views.loginU, name="login"),
    path('logout/', views.logoutU, name="logout"),
    path('registo/', views.registo, name="registo"),
    path('register/', views.registerU, name="register"),
]
