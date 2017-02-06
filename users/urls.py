from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^list/', ListView.as_view(), name="list_user"),
	url(r'^(?P<slug>[\w-]+)/$', ProfileView.as_view(), name="show_profile"),
	url(r'^(?P<slug>[\w-]+)/update/$', UpdateView.as_view(), name="update_profile"),
	url(r'^(?P<slug>[\w-]+)/delete/$', DeleteView.as_view(), name="delete_profile"),
	url(r'^(?P<slug>[\w-]+)/block/$', BlockView.as_view(), name="block_profile"),
]
