from django.conf.urls import include, url
from django.contrib import admin
from .views import(
    post_list,
    post_create,
    post_delete,
    post_update,
    post_detail,
    )
#from posts import views

urlpatterns = [
    # Examples:
    #url(r'^$', '.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    #url(r'^$', "posts.views.post_home"),




    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),


]
