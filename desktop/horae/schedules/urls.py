from django.conf.urls import url, patterns
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^my/$', views.my_schedule, name='my_schedule'),
	url(r'^request_cover/(\d+)/$', views.request_cover, name='request_cover'),
	url(r'^cover_shift/(\d+)/$', views.cover_shift, name='cover_shift'),
]