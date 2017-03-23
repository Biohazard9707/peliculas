from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from accounts import urls as accUrls
from main import urls as mainUrls
from catalogo import urls as catalogoUrls
from django.views.static import serve


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(accUrls, namespace="accounts")),
    url(r'^catalogo/', include(catalogoUrls, namespace="catalogo")),
    url(r'^', include(mainUrls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(
    	regex= r'^media/(?P<path>.*)$',
    	view = serve,
    	kwargs={'document_root':settings.MEDIA_ROOT}),
]
