from django.conf.urls import include, url
from django.contrib import admin
from .views import(

    donate_list,
    donate_create,
    donate_detail,


    )
urlpatterns = [
    # Examples:
    #url(r'^$', '.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    #url(r'^$', "posts.views.post_home"),



    url(r'^lists/$', donate_list, name='list'),
    url(r'^create/$', donate_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', donate_detail, name='detail'),


    #url(r'^posts/$', "<appname>.views.<function_name>"),


]
