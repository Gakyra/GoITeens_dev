from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('market.urls')),
    # path('example2/', include('example2.urls')),
    path("user_permission/", include('user_permission.urls')),
    path('example4/', include('example4.urls')),
    path('sygma/', include('sygma.urls')),
    path('mails/', include('mails.urls')),
    path('ajax_demo/', include('ajax_demo.urls'))


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
