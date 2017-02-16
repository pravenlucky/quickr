
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [

    url(r'^inventory/', include('inventory.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include("posts.urls", namespace='posts')),
    url(r'^$', include("posts.urls", namespace='posts2')),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
