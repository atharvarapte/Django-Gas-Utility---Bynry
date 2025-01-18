from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customer_service import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('service/', include('customer_service.urls')),
    path('admin/', admin.site.urls),
    path('service/', include('customer_service.urls')),
    path('', views.home, name='home'),  # Add this line for the root path
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



