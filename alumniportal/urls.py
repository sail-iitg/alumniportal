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
from alumniportal import forms_views, display_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', display_views.home , name='home'),
    url(r'^activity/$', display_views.activity , name='activity'),
    ####my edit
    url(r'^activity/$', forms_views.add_activity , name='add_activity'),
    url(r'^blog/edit/$', forms_views.blog_details_edit , name='blog_details_edit'),
    ##edit end
    url(r'^community/$', display_views.community , name='community'),
    url(r'^news/$', display_views.news , name='news'),
    url(r'^(?P<class_type>\b(news|activity)\b)/(?P<item_type>\b(All|add|Research|IITG|Student|Alumni|Achievement)\b)/$', display_views.items, name='news-items'),
    # url(r'^achievement/(?P<type>\b(all|iitg|alumni|student)\b)/$', display_views.items , name='news-items'),
    url(r'^profile/$', display_views.profile , name='profile'),
    url(r'^edit-profile/(?P<tab_type>\b(personal|professional|project|achievement|iitg|education)\b)/$', forms_views.edit_profile , name='edit-profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
