from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView


app_name = 'music'

urlpatterns =[
    url(r'^$', views.welcome, name='welcome'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^home/$', views.home, name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    url(r'^album(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
     # Home page for blog.
    url(r'^home/blogs/$', views.all_blogs, name='all_blogs'),
    # Show all topics.+Homepage
    url(r'^home/bloghome/$', views.blogs, name='blogs'),
    # Detail page for a single topic.
    url(r'^home/bloghome/blog/(?P<blog_id>\d+)/$', views.blog, name='blog'),
    # Page for adding a new topic.
    url(r'^home/bloghome/new_blog/$', views.new_blog, name='new_blog'),
    # Page for adding a new entry.
    # url(r'^home/bloghome/new_entry/(?P<blog_id>\d+)/$', views.new_chapter, name='new_chapter'),
    url(r'^home/bloghome/(?P<blog_id>[0-9]+)/delete_blog/$', views.delete_blog, name='delete_blog'),
    url(r'^home/bloghome/(?P<blog_id>\d+)/$', views.edit_blog,
        name='edit_blog'),
]
