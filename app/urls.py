from django.contrib import admin
from django.urls import path, include
from article.views import mainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('api/', include('article.urls')),
    path('', mainView),
]


from django.conf import settings
from django.conf.urls.static import static
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)