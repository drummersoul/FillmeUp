from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^list/$', ListView.as_view(), name="list_volunteer"),
	url(r'^add/$', CreateView.as_view(), name="add_volunteer"),
	url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(), name="show_volunteer"),
	url(r'^(?P<slug>[\w-]+)/update/$', UpdateView.as_view(), name="update_volunteer"),
	url(r'^(?P<slug>[\w-]+)/delete/$', DeleteView.as_view(), name="delete_volunteer"),
	url(r'^(?P<slug>[\w-]+)/block/$', BlockView.as_view(), name="block_volunteer"),
	url(r'^(?P<slug>[\w-]+)/report/$', ReportView.as_view(), name="report_volunteer"),
]
