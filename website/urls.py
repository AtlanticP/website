from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from companies import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
    url(r'^stocks/', views.StockList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:           # включить . Отключал для format_suffix_...
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Эта строка опциональна и будет добавлять url'ы только при DEBUG = True

# urlpatterns += staticfiles_urlpatterns()