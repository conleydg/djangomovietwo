from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

from . import views

app_name = 'movie_lens_online'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.movie, name='movie'),
    url(r'^rater/(?P<user_id>[0-9]+)/$', views.raterer, name='rater'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^top/(?P<genre>[a-zA-z]+)$', views.top_by_genre, name='top_by_genre'),
]
