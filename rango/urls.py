from django.conf.urls import patterns, include, url
from rango import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'askue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^about',views.about, name='about'),
)

