from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^list-movies/$', views.ListMovie.as_view(), name="list-movies"),
	url(r'^(?P<category_slug>[-\w]+)/$', views.ListMovie.as_view(), name="movie_list_category"),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.DetailMovie.as_view(), name="detail_movie"),
]