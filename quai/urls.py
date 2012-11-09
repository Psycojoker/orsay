from django.conf.urls import patterns, url
from django.views.generic import ListView

from models import Contact

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Contact), name='home'),
)
