from django.contrib import admin
from django.urls import include, path

from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("", include("catalog.urls")),
    path("", include("about.urls")),
]

if settings.DEBUG:
    urlpatterns += (path("___debug___/", include("debug_toolbar.urls")),)
