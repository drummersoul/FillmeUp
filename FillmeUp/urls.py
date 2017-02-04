from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from posts import views

urlpatterns = [
    # Examples:

    url(r'^$', 'posts.views.home', name='home'),
    url(r'^about_us/', 'posts.views.about_us',name='about_us'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/',include("posts.urls",namespace='posts')),
    url(r'^volunteer/', include('volunteer.urls', namespace="volunteer")),

    url(r'^accounts/', include('allauth.urls')),

    #url(r'^posts/$', "<appname>.views.<function_name>"),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
