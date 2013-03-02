from django.conf.urls import patterns, url

from views import home, PersonView

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^person/$', PersonView.as_view(), name="person_list"),
    url(r'^person/(?P<id>\d+)', PersonView.as_view(), name="person"),
)
