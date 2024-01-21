from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'VATS TRADING FLOOR'
admin.site.site_title = 'VTF'
admin.site.index_title= 'Dashboard'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Main.urls")),
    path("Content/", include("Content.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
