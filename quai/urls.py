from django.conf.urls import patterns, url
from django.views.generic import ListView

from models import Person

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Person), name='home'),
)
