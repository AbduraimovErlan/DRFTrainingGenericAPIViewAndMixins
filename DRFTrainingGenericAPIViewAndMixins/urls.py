from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('GenericAPIVewAndMixins1.urls')),
    path('api/v1/', include('GenericAPIVewAndMixins2.urls')),
    path('api/v1/', include('GenericAPIVewAndMixins3.urls')),
    path('api/v1/', include('GenericAPIVewAndMixins4.urls')),
    path('api/v1/', include('GenericAPIVewAndMixins5.urls')),
    path('api/v1/', include('GenericAPIVewAndMixins6.urls')),
    path('api/v1/', include('GenericAPIVewAndMixins7.urls')),
    path('api/v1/', include('GenericAPIVewAndMixins8.urls')),
    path('api/v1/', include('GenericAPIVewAndMixins9.urls')),
]
