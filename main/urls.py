from django.contrib import admin
from django.urls import path, include
from home.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('home/', index, name='index'),
    path('catalog/', include('home.urls', namespace='catalog')),
    path('users/', include('users.urls', namespace='users')),
    path('orders/', include('orders.urls', namespace='orders')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)