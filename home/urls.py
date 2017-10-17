from django.conf.urls import url
from . import views


app_name='home'
urlpatterns = [
	url(r'^$', views.index, name='main'),
	url(r'^events$', views.events, name='events'),
	url(r'^magic$', views.magic, name='magic')
]