from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_change, password_change_done
from . import views

urlpatterns = [
	url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
	url(r'^registry/$', views.RegistryView.as_view(), name='registry'),
	url(r'^login/$', login, name='login'),
	url(r'^logout/$', logout, name='logout'),
	#Cambio de contraseña
	# url(r'^password-change/$', password_change, name="password_change"),
	# url(r'^password-change/done/$', password_change_done, name="password_change_done"),
]