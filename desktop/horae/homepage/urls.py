from django.conf.urls import url, patterns
from . import views

urlpatterns = [
	url(r'$', views.index, name='index')
]
