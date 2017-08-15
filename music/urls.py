from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'music'

urlpatterns = [
	
	# url(r'get_object/$', views.get_object, name = 'get_object'), #для отладки
	
	url(r'^register/$', views.UserFormView.as_view(), name = 'register'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'details'),
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name = 'album-delete'),
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name = 'album-update'),
    url(r'album/add/$', views.AlbumCreate.as_view(), name = 'album-add'),
    url(r'^$', views.IndexView.as_view(), name = 'index'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	