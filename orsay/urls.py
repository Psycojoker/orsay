from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    # url(r'^orsay/', include('orsay.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
