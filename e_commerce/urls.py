from atexit import register
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path

from register import views as vr


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('register/', vr.register, name='register'),
    path('api/v1/', include('e_commerce_api.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)