from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path




urlpatterns = [    
    path('admin/', admin.site.urls),
    path('', include('books.urls',  namespace='books')),
    path('', include('search.urls', namespace='search')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)