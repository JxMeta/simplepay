from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tag/(?P<tag_name>[^/]+)/$', views.tag, name='tag'),
    url(r'^person/(?P<person_name>[^/]+)/$', views.person, name='person'),
]
