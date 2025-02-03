
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('' , include('Estudios.urls')),
    path('admin/', admin.site.urls),
]
from django.conf.urls import handler404

handler404 = 'Estudios.views.Status404'


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)