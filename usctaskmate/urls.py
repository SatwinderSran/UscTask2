from django.contrib import admin
from django.urls import path, include
from usc import views as usc_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', usc_views.index, name='index'),
    path('usc/', include('usc.urls')),
    path('account/', include('users_app.urls')),   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   