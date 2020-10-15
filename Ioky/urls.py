from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('about/', include('about.urls')),
    path('for-partners/', include('forPartners.urls')),
    path('projects/', include('projects.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)