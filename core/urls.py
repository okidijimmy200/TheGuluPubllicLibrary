from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [    
    path('admin/', admin.site.urls),
    path('', include('books.urls',  namespace='books')),
    path('', include('search.urls', namespace='search')),
    url(r'^accounts/', include('allauth.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)