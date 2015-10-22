"""iitg URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from alumniportal import views

urlpatterns = [
    url(r'^$', views.home , name='home'),
    url(r'^activity/$', views.activity , name='activity'),
    ####my edit
    url(r'^activity/add/$', views.add_activity , name='add_activity'),
    url(r'^blog/edit/$', views.blog_details_edit , name='blog_details_edit'),
    ##edit end
    url(r'^community/$', views.community , name='community'),
    url(r'^news/$', views.news , name='news'),
    url(r'^profile/$', views.profile , name='profile'),
    url(r'^news-list/$', 'alumniportal.views.news_list' , name='news-list'),
    url(r'^edit-profile/$', views.edit_profile , name='edit-profile'),
]
