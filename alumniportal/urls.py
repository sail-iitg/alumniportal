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
    url(r'^news/$', display_views.news , name='news'),
    url(r'^volunteer/$', display_views.volunteer),
    url(r'^community/$', display_views.community , name='community'),
    
    ####my edit
    # url(r'^activity/(?P<item_type>.*)/$', display_views.activity_items),
    # url(r'^activity/(?P<item_type>\b(event|meet|volunteer|survey|project)\b)/$', display_views.activity_items),
    # url(r'^volunteer/add/$', forms_views.add_volunteer),
    ##edit end
    
    # url(r'^(?P<class_type>\b(activity|news)\b)/add/$', forms_views.add, name='add'),
    url(r'^news/add/$', forms_views.add_news, name='add-news'),
    url(r'^activity/add/$', forms_views.add_activity , name='add_activity'),

    url(r'^(?P<class_type>\b(news)\b)/(?P<item_type>\b(All|Research|IITG|Student|Alumni|Achievement)\b)/$', display_views.items, name='news-items'),
    url(r'^(?P<class_type>\b(activity)\b)/(?P<item_type>\b(All|Event|Alumni Meet|Volunteering|Survey|Project)\b)/$', display_views.items, name='activity-items'),
    url(r'^(?P<class_type>\b(activity|news|community)\b)/(?P<id>.+)/edit/$', forms_views.edit, name='edit'),
    url(r'^(?P<class_type>\b(activity|news|community)\b)/(?P<id>.+)/$', display_views.detail, name='detail'),
    
    # url(r'^achievement/(?P<type>\b(all|iitg|alumni|student)\b)/$', display_views.items , name='news-items'),
    url(r'^profile/$', display_views.profile , name='profile'),
    url(r'^profile/change-password/$', display_views.change_password , name='change_password'),
    url(r'^profile/(?P<profile_id>.*)/$', display_views.view_profile , name='view-profile'),
    url(r'^search/$', display_views.search),

    url(r'^edit-profile/personal/$', forms_views.edit_personal , name='edit-personal'),
    url(r'^edit-profile/$', forms_views.edit_personal , name='edit-profile'),
    url(r'^edit-profile/professional/$', forms_views.edit_professional , name='edit-professional'),
    url(r'^edit-profile/professional/current/$', forms_views.current , name='current'),

    url(r'^edit-profile/education/$', forms_views.edit_education , name='edit-education'),
    url(r'^edit-profile/education/current/$', forms_views.current , name='current'),
    url(r'^edit-profile/achievement/$', forms_views.edit_achievement , name='edit-achievement'),
    url(r'^edit-profile/iitg/$', forms_views.edit_iitg , name='edit-iitg'),
    url(r'^edit-profile/project/$', forms_views.edit_project , name='edit-project'),
    url(r'^edit-profile/blog/$', forms_views.edit_blog_details , name='edit-blog-details'),

    # url(r'^(?P<news_id>\d+)/edit/news/$', forms_views.edit_news, name='edit-news'),
    # url(r'^(?P<news_id>\d+)/news/$', display_views.news_detail, name='news-detail'),


    url(r'^blog/(?P<username>.+)/post/add/$', forms_views.add_post, name='add-post'),
    url(r'^blog/(?P<username>.+)/post/(?P<post_id>\d+)/edit/$', forms_views.edit_post, name='edit-post'),
    url(r'^blog/(?P<username>.+)/post/(?P<post_id>\d+)/comment/$', forms_views.add_post_comment, name='post-comment'),
    url(r'^blog/(?P<username>.+)/post/(?P<post_id>\d+)/list-comments/$', forms_views.post_comments_list, name='post-comment-list'),
    url(r'^blog/(?P<username>.+)/post/(?P<post_id>\d+)/$', display_views.post_detail, name='post-detail'),
    url(r'^blog/(?P<username>.+)/$', display_views.blog, name='blog'),
    url(r'^blog/$', display_views.blog, name='blog'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
