from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from account.views import loginPage, logoutPage, registerPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('kb/', include('article.urls')),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('register/', registerPage, name='register'),
    path('', include('article.urls')),
]


from django.conf import settings
from django.conf.urls.static import static
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)